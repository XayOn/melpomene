melpomene
-----------------------------

.. image:: https://travis-ci.org/XayOn/melpomene.svg?branch=master
    :target: https://travis-ci.org/XayOn/melpomene

.. image:: https://coveralls.io/repos/github/XayOn/melpomene/badge.svg?branch=master
 :target: https://coveralls.io/github/XayOn/melpomene?branch=master

.. image:: https://badge.fury.io/py/melpomene.svg
    :target: https://badge.fury.io/py/melpomene

Search a video or subset of a video on google
Requires python3.7


Usage
-----

::

    Usage: melpomene [OPTIONS]

          Search for all given frames of a video in google images.

          Stops after a specific number of results have been met. You can specify a
          step for video frame extraction.

          This requires to have a base_path where all extracted frames will be
          stored, that is actually accessible trough a external url. ngrok can be
          used for exposing a directory with:

              mkdir images     cd images     python -m http.server 8080 & ngrok http
              8080

          base_path will be "images" and ngrok_url will be
          http://ngrok.io/<your_ngrok_url>/images

        Options:
          --video TEXT      video file  [required]
          --url TEXT        public url to base path  [required]
          --base_path TEXT  path to store images
          --end INTEGER     stop after <end> results
          --step INTEGER    parse each <step> frames
          --help            Show this message and exit.


Distributing
------------

Distribution may be done in the usual setuptools way.
If you don't want to use pipenv, just use requirements.txt file as usual and
remove Pipfile, setup.py will auto-detect Pipfile removal and won't try to
update requirements.

Note that, to enforce compatibility between PBR and Pipenv, this updates the
tools/pip-requires and tools/test-requires files each time you do a *dist*
command

General notes
--------------

This package uses PBR and pipenv.
Pipenv can be easily replaced by a virtualenv by keeping requirements.txt
instead of using pipenv flow.
If you don't need, or you're not actually using git + setuptools distribution
system, you can enable PBR manual versioning by creating a METADATA file with
content like::

    Name: melpomene
    Version: 0.0.1

Generating documentation
------------------------

This package contains a extra-requires section specifiying doc dependencies.
There's a special hook in place that will automatically install them whenever
we try to build its dependencies, thus enabling us to simply execute::

        pipenv run python setup.py build_sphinx

to install documentation dependencies and buildd HTML documentation in docs/build/


Passing tests
--------------

Running tests should always be done inside pipenv.
This package uses behave for TDD and pytest for unit tests, you can execute non-wip
tests and behavioral tests using::

        pipenv run python setup.py test


Docker
------

This package can be run with docker.

Default entry_point will be executed (melpomene) by default

This builds the docker for a SPECIFIC distributable release, that you need to
have previously built.

For this, do a release::

    python setup.py sdist

Grab the redistributable files::

    distrib=($(/bin/ls -t dist))

Now run docker build with it::

    docker build --build-arg distfile=${distrib[1]}
