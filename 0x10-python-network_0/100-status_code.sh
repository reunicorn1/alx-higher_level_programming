#!/bin/bash
# This script requests a URL and displays the status code of the reposne
curl -s -o /dev/null -w "%{http_code}" "$1" 
