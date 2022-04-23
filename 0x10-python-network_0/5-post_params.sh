#!/bin/bash
# This bash script sends a POST request to the URL passed alog with some parameters, and displays the body of the response.
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
