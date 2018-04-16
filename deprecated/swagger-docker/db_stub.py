from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
def get_database():
	client = MongoClient("localhost", 27017)
	db=client.test_database
	answer = {}
	# pprint(client.test_database)
	# Issue the serverStatus command and print the results
	serverStatusResult=db.command("serverStatus")
	# pprint(serverStatusResult)
	answer['name']=serverStatusResult['host']
	ca=str(client.address[0])+':'+str(client.address[1])
	answer['endpoint']=ca
	answer['protocol']=serverStatusResult['process']
	return answer
	# pprint(client.address)
	# pprint(serverStatusResult['host'])
	# pprint(serverStatusResult['process'])