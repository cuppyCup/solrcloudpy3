#!/usr/bin/env python3

from distutils.core import setup

setup(name='solrcloudpy3',
      version='0.1a',
      description='Solr CLOUD API for Python 3.5 and Solr 6.3.0.  This is a fork of the code base posted '
                  + 'at https://github.com/solrcloudpy/solrcloudpy .',
      author='Matthew Barrett & the Open Source Community',
      author_email='matthew.robert.barrett@gmail.com',
      url='https://www.github.com/cuppyCup/solrclodupy3/',
      packages=['solrcloudpy3', 'solrcloudpy3.collection'],
)