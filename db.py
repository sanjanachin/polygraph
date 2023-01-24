from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING = "mongodb+srv://polygraph:polygraph#123@cluster0.w5ydh5i.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Cluster0')
user_collection = pymongo.collection.Collection(db, 'user_collection')