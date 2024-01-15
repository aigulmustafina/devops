#!/usr/bin/env bash
set -euo pipefail

docker-compose up -d
sleep 3
docker exec -it rabbit-2 rabbitmqctl stop_app
docker exec -it rabbit-2 rabbitmqctl reset
docker exec -it rabbit-2 rabbitmqctl join_cluster rabbit@$(docker ps -q -f "name=rabbit-1")
docker exec -it rabbit-2 rabbitmqctl start_app
