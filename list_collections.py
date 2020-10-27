#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb
    print(db.list_collection_names())