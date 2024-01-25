#!/bin/bash
# script that send GET request, and display the body of the response
curl -X GET -sI $1 | grep -w 'Content-Length' | awk '{print $2}'