#!/bin/bash
# Sends POST request with header variables to a given URL and displays the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
