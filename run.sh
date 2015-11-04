#!/usr/bin/env bash

>properties.json
scrapy runspider scrape.py -t json -o properties.json
#cat properties.json | jq '.'
