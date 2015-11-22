#!/usr/bin/env bash

set -e

which scrapy > /dev/null || sudo pip install Scrapy

>properties.json
scrapy runspider scrape.py -t json -o properties.json
#cat properties.json | jq '.'
