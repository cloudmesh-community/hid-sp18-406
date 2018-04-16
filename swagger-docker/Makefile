SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=db.yaml
DESTDIR=server/db/flaskConnexion
CREATED=server

all: service start 
	@echo "DONE"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build -t ramyadg/cloudmesh-dbinfo .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull ramyadg/cloudmesh-dbinfo
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 ramyadg/cloudmesh-dbinfo

docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f ramyadg/cloudmesh-dbinfo
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)
	 
service: dest
	@echo "creating the service..."
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython3=true
	
	rm *.jar
	pip install --upgrade pip
	pip install pymongo

	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cp database.py $(DESTDIR)/swagger_server/models
	cp base_model_.py $(DESTDIR)/swagger_server/models
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 
	
	

start:  
	@echo "starting the service..."
	mongod --bind_ip 0.0.0.0 --noauth
	service mongodb start
	service mongodb status
	cd $(DESTDIR) && python -m swagger_server

test:
	curl http://localhost:8080/api/db
            
stop:
	@echo "stopping the service"
	ps -ef | grep swagger_server | grep -v "grep" | awk '{print $$2}' | xargs kill -9
	@echo "service stopped"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)

