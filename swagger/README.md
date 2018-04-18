# Assignment: Cloud and Big Data Rest Service with Swagger

### Service Descprition

*Built a Database service that will provide following capabilities* 

* Provides the Endpoint of the client
* Provide Hostname of the client
* Provides Protocol name of the client (Ex: Mongod)

Here, I have implemented a Database object that will return database attributes.
The swagger code-gen generate the server stub code for us by taking the 
db.yaml as input and gives us a foundation to develop the main logic.
Main logic : *db_stub.py*
Location - 
https://github.com/cloudmesh-community/hid-sp18-406/blob/master/swagger/flaskConnexion/swagger_server/controllers/db_stub.py


You can download the code from the repository and test or enhance further.

### Follow the below steps

* Clone the repository
* Run the Database service in the MongoDB background
	If the mongod service is not installed, install the service by following the steps given in this link
	https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
* Start the mongod service <br />   
	``sudo service mongod start``   	
* Navigate to "flaskConnexion" directory <br />
* Install pymongo and connexion if not present, <br />
``pip install pymongo`` <br/> 
``pip install connexion`` <br />
* Start the service by executing the command ``python -m swagger_server``

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
    "name": "dg-HP-Pavilion-Notebook",
    "protocol": "mongod"
  }
}





