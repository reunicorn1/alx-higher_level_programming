#!/bin/bash
# This script takes a URL and sends a request, and finally displays the size of the body of the response
curl -sI $1 | awk '/Content-Length/{print $2}'
