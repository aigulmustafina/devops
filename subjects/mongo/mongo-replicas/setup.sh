#!/usr/bin/env bash
set -euo pipefail

docker-compose up -d
docker exec -i mongo-replicas_mongo-1_1 mongo << EOF
rsconf={_id: "testingSet", members: [
        {_id: 0, host: "mongo-1:27017"},
        {_id: 1, host: "mongo-2:27018"},
        {_id: 2, host: "mongo-3:27019"}]}
rs.initiate(rsconf)
EOF

curl -sLO https://stepik.org/media/attachments/lesson/705682/mongo-dump.tar.gz
tar -xvf mongo-dump.tar.gz
docker cp reservations mongo-replicas_mongo-1_1:/reservations

docker exec -i mongo-replicas_mongo-1_1 mongorestore -d reservations /reservations
