CONTAINER=$(docker run \
--publish=7474:7474 \
--publish=7687:7687 \
--volume=/Users/xin/project/knowledge_base_construction/kbc/db_file/neo4j/data:/data \
--volume=/Users/xin/project/knowledge_base_construction/kbc/db_file/neo4j/logs:/var/lib/neo4j/logs \
--volume=/Users/xin/project/knowledge_base_construction/kbc/db_file/neo4j/import:/var/lib/neo4j/import \
--env=NEO4J_AUTH=neo4j/kbcdata \
--env=NEO4J_dbms_memory_heap_initial__size=1G \
--env=NEO4J_dbms_memory_heap_max__size=3G \
--name neo4j_kbc \
-d neo4j)
echo "running neo4j, waiting for startup"
