#!/bin/bash
# This script takes a URL and displays all HTTP methods that the server will accept
curl -sI "$1"| awk '/Allow:/{print $2}' 
