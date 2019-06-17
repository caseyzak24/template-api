#!/usr/bin/env bash
docker-compose -f docker-compose.yml -f e2e/docker-compose.e2e.yml build && \
    docker-compose -f docker-compose.yml -f e2e/docker-compose.e2e.yml up -d
docker-compose -f docker-compose.yml -f e2e/docker-compose.e2e.yml down
