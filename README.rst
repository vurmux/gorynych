.. -*- mode: rst -*-

.. image:: https://travis-ci.org/vurmux/gorynych.svg?branch=master
           :target: https://travis-ci.org/vurmux/gorynych


Gorynych
========

Gorynych is an automatic data scraping and extracting system.
The main difference between this package and existing spider systems is that
Gorynych automatically extracts only useful information from the scraped text.

**This project is in very early stage of development.**
**Keep in mind that it is unstable and has no backward compatibility!**


Dependencies
============

Gorynych is designed to work under Python >=3.4.

The required dependencies for this package are:

- beautifulsoup4
- requests
- nltk (for default mining engine)

Additional mining engines require more packages:

- OpenCog Relex
- link-grammar


Installation
============

This package uses setuptools for installation.

To install in your home directory, use:

- python setup.py install --user

To install for all users:

- sudo python setup.py install
