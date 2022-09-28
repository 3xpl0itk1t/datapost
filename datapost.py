import json
from pymongo import MongoClient
from dateutil import parser
import datetime
MONGO = "" # url to the mongodb server

cluster = MongoClient(MONGO)
db = cluster[""] # cluster name
collection = db[''] # collection name

f = open('') # json file

y = json.loads(f.read())

for i in y:


  obj = {
      'key' : 'val' # key val pair as per the db schema and json file
  }
  collection.insert_one(obj)

  print(obj)