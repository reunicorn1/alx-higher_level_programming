#!/bin/bash
# This script sends JSON POST request and displays body of response
curl -s -d @"$2" --header "Content-Type: application/json" --header "Accept: application/json" "$1"
