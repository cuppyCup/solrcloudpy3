#!/bin/sh

set -e

# Deploy the module to PyPI
echo "Deploying solrcloudpy3 to PyPI."
python setup.py sdist upload -r pypi
