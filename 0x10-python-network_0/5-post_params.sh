#!/bin/bash
# This script taks a URL, sends POST request to the passed URL and displays the body of the response
curl -sd email=test@gmail.com -d subject="I will always be here for PLD" "$1"
