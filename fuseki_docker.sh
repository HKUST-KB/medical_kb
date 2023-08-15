docker run -p 3030:3030 -e JVM_ARGS=-Xmx2g -e ADMIN_PASSWORD=pw123 \
	-v /data/kbc_data/db_file/fuseki/data:/fuseki \
	-v /data/kbc_data/db_file/fuseki/import://staging \
	--name fuseki \
 	-d stain/jena-fuseki
