docker exec -it `docker ps -f ancestor=neo4j -q` bin/cypher-shell -u neo4j -p kbcdata
