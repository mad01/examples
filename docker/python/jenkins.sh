#!/usr/bin/env bash
set -o errexit
set -o xtrace
set -o pipefail

docker-compose build --no-cache
docker-compose run tester
