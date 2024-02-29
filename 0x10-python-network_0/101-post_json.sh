#!/bin/bash
# This script sends JSON POST request and displays body of response
curl -s --json @"$2" "$1"
