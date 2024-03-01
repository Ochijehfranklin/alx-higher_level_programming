#!/bin/bash
# Diplay size of body response
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
