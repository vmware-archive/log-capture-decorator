#!/usr/bin/env bash

set -ex

mkdir -p ./tmp

rm -rf ./tmp/log-capture-buildpack.zip
zip -r ./tmp/log-capture-buildpack.zip bin/* lib

cf delete-buildpack log-capture-buildpack -f
cf create-buildpack log-capture-buildpack ./tmp/log-capture-buildpack.zip 99 --enable
