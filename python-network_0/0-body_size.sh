#!/bin/bash

# Check if URL is provided
[ $# -eq 0 ] && { echo "Usage: $0 <URL>"; exit 1; }

# Fetch Content-Length from URL and display the size
url=$1; response_body=$(curl -sI $url | awk '/Content-Length/ {print $2}' | tr -d '\r'); [ -z "$response_body" ] && { echo "Error: Content-Length header not found in the response."; exit 1; }; echo "Size of the response body: ${response_body} bytes"
