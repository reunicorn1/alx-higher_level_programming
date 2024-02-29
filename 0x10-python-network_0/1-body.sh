#!/bin/bash
# This script take a URL and sends GET request and displays the body of the response
response=$(curl -sI -L "$1" | awk '/HTTP/{print $2}' | grep 200)
if [ "$response" == "200" ]
then
        curl -sL "$1"
fi
