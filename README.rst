.. -*- mode: rst -*-

.. |Travis| image:: https://api.travis-ci.org/vurmux/gorynych.svg?branch=master
.._Travis: https://travis-ci.org/vurmux/gorynych


Gorynych
========

Gorynych is an automatic data scraping and extracting system.
The main difference between this package and existing spyder systems is that
Gorynych automatically extracts useful information from scraped text.

**This project is in very early stage of development.**
**Keep in mind that it is unstable and has no backward compatibility!**


Dependencies
============

Gorynych is tested to work under Python 3.4. But it should also work with Python 3.2-3.5.

The required dependencies for this package are:

- beautifulsoup4
- requests
- nltk (for default mining engine)


Installation
============

This package uses setuptools for installation.

To install in your home directory, use:

python setup.py install --user

To install for all users:

sudo python setup.py install
