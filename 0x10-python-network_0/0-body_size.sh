#!/usr/bin/env bash
# script to get the body size of a request
curl -sI "$1" | grep Content-Length | cut -f2 -d ' '
