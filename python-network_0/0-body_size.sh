#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Use curl to send a request to the URL and store the response body in a variable
response_body=$(curl -sI $url | awk '/Content-Length/ {print $2}' | tr -d '\r')

# Check if Content-Length header is present in the response
if [ -z "$response_body" ]; then
    echo "Error: Content-Length header not found in the response."
    exit 1
fi

echo "Size of the response body: ${response_body} bytes"
