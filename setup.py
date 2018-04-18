#!/usr/bin/python3


from setuptools import setup, find_packages
from codecs import open
from os import path, mkdir


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gorynych',
    version='0.0.1',
    description='Automatic data collecting and refining system',
    long_description=long_description,
    url='https://github.com/vurmux/gorynych',
    author='Andrey Voronov',
    author_email='vurmux@gmail.com',
    license='Apache',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Information Technology',
        'Topic :: Internet',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='scraping osint',
    packages=find_packages(exclude=['docs', 'img']),
    install_requires=['networkx'],
    extras_require={
        'dev': [],
        'test': ['coverage'],
    },
    package_data={
        'gorynych': ['*.txt', '*.json'],
    },
    entry_points={
        'console_scripts': [
            'gorynych-daemon=gorynych.gorynych_daemon:main',
        ],
    },
)

# Post-installation script
gch_home_folder = path.join(
    path.expanduser('~'),
    'gorynych'
)
if not path.exists(gch_home_folder):
    mkdir(gch_home_folder)
