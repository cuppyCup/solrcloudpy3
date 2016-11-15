#!/usr/bin/env python3

from distutils.core import setup
import re
from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()


def get_version():
    return re.search(r"""__version__\s+=\s+(?P<quote>['"])(?P<version>.+?)(?P=quote)""",
                     open('solrcloudpy3/__init__.py').read()).group('version')

setup(name='solrcloudpy3',
      version=get_version(),
      description='Solr CLOUD API for Python 3.5 and Solr 6.3.0.  This is a fork of the code base posted '
                  + 'at https://github.com/solrcloudpy/solrcloudpy .',
      author='Didier Deshommes, Robert Elwell, Matthew Barrett',
      author_email='matthew.robert.barrett@gmail.com',
      url='https://www.github.com/cuppyCup/solrclodupy3/',
      license='LICENSE.txt',
      keywords='solr solrcloud',
      platforms='any',
      entry_points={'console_scripts': ['solrconsole = scripts.solrconsole:main [ip]']},
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
        ],

      install_requires=['requests >= 2.2.1', 'IPython >= 1.2.0', 'semver == 2.4.1'],
      extras_require={"ip": ['IPython >= 1.2.0']},
      packages=["solrcloudpy3", "solrcloudpy3.collection"]
)