#! /bin/bash
docker build -t bdo .
docker stop bdo
docker rm bdo
docker run -v $(pwd):/bdo --name {[package}} -dt bdo bash
docker exec -it bdo bash
