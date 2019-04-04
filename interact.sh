#!/bin/bash
CONTAINER=${1:-"app"}
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
sleep 1.5
docker exec -it "${CONTAINER}" /bin/bash
