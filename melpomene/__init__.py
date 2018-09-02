"""melpomene.

Search a video or subset of a video on google
"""

from itertools import takewhile, repeat, islice
from operator import itemgetter
from pathlib import Path
import tempfile

from requests_html import HTMLSession
import click
import cv2
import numpy

SESSION = HTMLSession()

URL = 'https://www.google.com/searchbyimage?&image_url={}'


def search_google_images(image, base_path, ngrok_url):
    """Return all exact search results from google images."""
    with tempfile.NamedTemporaryFile(suffix='.jpg', dir=base_path) as fileo:
        _, img = cv2.imencode('.jpg', image)
        fileo.write(numpy.array(img).tostring())
        result = SESSION.get(URL.format(ngrok_url + Path(fileo.name).name))
        print(result.url)
    yield from result.html.find('h3.r>a')


def get_images(vid, step):
    """Extract each <step> images from a cv2 video capture file."""
    yield from (elem for num, (_, elem) in enumerate(
        takewhile(itemgetter(0), repeat(vid.read()))) if num % step == 0)


def execute_search(video, base_path, ngrok_url, step):
    """Execute a search for each extracted image of the video"""
    for image in get_images(cv2.VideoCapture(video), step):
        yield from search_google_images(image, base_path, ngrok_url)


@click.command()
@click.option('--video', help='video file', required=True)
@click.option('--url', help='public url to base path', required=True)
@click.option('--base_path', help='path to store images', default='images')
@click.option('--end', help='stop after <end> results', default=10)
@click.option('--step', help='parse each <step> frames', default=1)
def main(video, base_path, url, end, step):
    """Search for all given frames of a video in google images.

    Stops after a specific number of results have been met.
    You can specify a step for video frame extraction.

    This requires to have a base_path where all extracted frames will be
    stored, that is actually accessible trough a external url.
    ngrok can be used for exposing a directory with:

        mkdir images
        cd images
        python -m http.server 8080 & ngrok http 8080

    base_path will be "images"
    and ngrok_url will be http://ngrok.io/<your_ngrok_url>/images

    """
    result = islice(execute_search(video, base_path, url, step), end)
    print(list(set((a.attrs.get('href') for a in result))))
