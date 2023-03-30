#!/bin/bash
# Sends GET request with header variable "X-School-User-Id" = 98 to a given URL and displays the body of the response
curl -sX GET -H "X-School-User-Id:98" "$1"
