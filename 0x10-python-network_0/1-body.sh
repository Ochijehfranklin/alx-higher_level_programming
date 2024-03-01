#!/usr/bin/bash
# This cURL to the end

curl -s -o /dev/null -w "%{http_code}\n" $1 | grep 200 && curl -s $1
