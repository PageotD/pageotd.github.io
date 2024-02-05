#!/bin/bash

docker build -t ghpage .
docker run --rm -p 8080:80 --name ghpage_nginx ghpage
