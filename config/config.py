from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Use this connection string in your application known as database URL Endpoint : 

uri = " { Use this connection string in your application known as database URL Endpoint } "

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Blogging 
blogs_collection = db["blogs"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)