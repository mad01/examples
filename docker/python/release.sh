#!/usr/bin/env bash
set -o errexit
set -o xtrace
set -o pipefail

pip2 install -r requirements.txt
nosetests-2.7 tests
bumpversion $1
make clean
python setup.py sdist
# twine upload dist/* --config-file=<.pypirc> --repository <private> -p "" -u ""
git push --tags
git push 
