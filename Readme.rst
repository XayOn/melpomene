Video Searcher
--------------

Requires python3.7

Usage: pipenv run python searcher.py [OPTIONS]

  Search for all given frames of a video in google images.

  Stops after a specific number of results have been met. You can specify a
  step for video frame extraction.

  This requires to have a base_path where all extracted frames will be
  stored, that is actually accessible trough a external url. ngrok can be
  used for exposing a directory with::

      mkdir images
      cd images
      python -m http.server 8080 & ngrok http 8080

  base_path will be "images" and ngrok_url will be
  http://ngrok.io/<your_ngrok_url>/images


::

        Options:
          --video TEXT      video file
          --base_path TEXT  path to store images
          --ngrok_url TEXT  public ngrok url to base path
          --end INTEGER     stop after <end> results
          --step INTEGER    parse each <step> frames
          --help            Show this message and exit.

