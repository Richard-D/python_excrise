from pymongo import MongoClient
import requests,json
url = ""
client = MongoClient("localhost",27017)
db = client['test-database']
collection = db.test_collection