#!/bin/bash
# This bash script sends a POST request to the URL passed in the form of JSON data, and displays the body of the response.
curl -X POST -sH 'Content-Type: application/json'" -d "$2" "$1"
