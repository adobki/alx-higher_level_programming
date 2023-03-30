#!/bin/bash
# Sends request to a given URL and displays only the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
