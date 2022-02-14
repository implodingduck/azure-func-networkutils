#!/bin/bash
docker stop networkutilfunction
docker container rm networkutilfunction
docker build -t networkutilfunction .
docker run -p 8000:80 -d --name networkutilfunction networkutilfunction
