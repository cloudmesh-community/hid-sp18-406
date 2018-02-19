# Assignment: Cloud and Big Data Rest Service with Swagger

### Service Descprition

*Built a Database service that will provide following capabilities* 

* Provides the Endpoint of the client
* Provide Hostname of the client
* Provides Protocol name of the client (Ex: Mongod)

Here, I have implemented a Databse object that takes client database host URL
name as the input in the form of query parameter.
The swagger code-gen generate the server stub code for us by taking the 
time.yaml as input and gives us a nice foundation to develop the main logic.
Main logic : *db_stub.py*
Location - 
https://github.com/cloudmesh-community/hid-sp18-406/blob/master/swagger
/flaskConnexion/swagger_server/controllers/db_stub.py


You can download the code from the repository and test or enhance further.

### Follow the below steps

* Clone the repository
* Run the Database service in the backgorund
* Navigate to "flaskConnexion" directory 
* Start the service by executing the command "python -m swagger_server"

You will see something like this 
Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)


### Running the service from browser


* Open any browser and request with DB_URL
Ex:
Input : http://0.0.0.0:8080/api/db
Output :
{
  "database": {
    "endpoint": "localhost:27017",
    "name": "manoj-HP-Pavilion-Notebook",
    "protocol": "mongod"
  }
}





