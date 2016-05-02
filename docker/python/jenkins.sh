#!/usr/bin/env bash
set -o errexit
set -o xtrace
set -o pipefail

cp $HOME/.ssh/id_rsa id_rsa_docker
cp $HOME/.ssh/id_rsa.pub id_rsa_docker.pub

docker-compose build --no-cache
docker-compose run tester
