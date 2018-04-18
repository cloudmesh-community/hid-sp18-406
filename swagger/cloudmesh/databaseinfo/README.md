# Swagger Database Description for MongoDB service on Docker

## Acknowledgement 
Thanks to Shagufta and Karan Kamatgi for giving us a starting point in implementing this service on docker.

## Implementation :
* The specification of the Swagger REST service is defined in the YAML file `db.yaml` file
* Database description generation logic has been implemented in the stub file `db_stub.py`
* The implemented database service will provide the following information
	a. Displays endpoint of the client
	b. Displays Hostname of the client
	c. Displays Protocol name of the client, here it is implemented for MongoDB

## Steps for Execution :

* Clone the repository <br />
	`git clone https://github.com/cloudmesh-community/hid-sp18-406.git`

* Navigate to th docker service directory <br \>

        `cd /hid-sp18-406/swagger/cloudmesh/databaseinfo`


* Using docker to run the Database Description swagger service :

	- `make docker-all` -- actually creates the docker image, 
	starts the container and runs the service(Mandatory to execute)

* For optional Debug purpose
	- `make docker-build` -- creates the docker image only

	- `make docker-start` -- starts the container and runs the REST service

	- `make docker-stop` -- stops the container 

	- `make docker-remove` -- removes the docker image

	- `make docker-clean` -- stops the container and remove the image
  
* Test the service :
  Mongo service will be up and running, check the below API in browser 
  
  	for example - `http://0.0.0.0:8080/api/db`
	
	This URL is verified in Google Chrome and Mozilla FireFox.

  Please make sure to run the following command in a seperate terminal after 
  running `make docker-all`
  
  	`make docker test` -- curl for the database description details

  Output
	`{ <br />
  	  "database": { <br />
    	  "endpoint": "172.17.0.2:27017", <br /> 
          "name": "929f3e238ba0", <br />
   	  "protocol": "mongod" <br />
 	   } <br />
	}`



## Service Descprition

This swagger REST service aims at exposing the database details of 
MongoDB database residing on the host container. The basic idea is to
create a docker container with all the implementation details and 
create another image to host MongoDB, linking these images helped
me to connect the two images and extract the database details
thourgh API or curl test command.






