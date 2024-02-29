#!/bin/bash
# This script take a URL and sends GET request and displays the body of the response
response=$(curl -sI $1| awk '/HTTP/{print $2}')
if [ "$response" == "200" -o "$response" == "302" ]
then
	curl -L $1
fi
