#!/bin/bash
# Displays all the HTTP methods the server at the given URL will accept
curl -siX OPTIONS "$1" | grep -oP '(?<=Allow: ).*'
