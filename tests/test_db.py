from flask import Flask
from flask_pymongo import pymongo
import pytest

CONNECTION_STRING = "mongodb+srv://polygraph:a1JbnPxslP8gN3Sm@cluster0.w5ydh5i.mongodb.net/?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(CONNECTION_STRING)
db = cluster["Cluster0"]
data = pymongo.collection.Collection(db, "test_users")

def add_test_data():
    topics = ["vaccines", "legislation", "conspiracy", "foreign affairs", "pseudoscience", "COVID-19", "election fraud"]
    for i in range(100):
        post = {"_id": "user" + str(i), "history": [topics[0:(i % len(topics))]]}
        data.update_one({"_id": "user" + str(i)}, {"$set":post}, upsert=True)

add_test_data()

def test_retrieve_history_from_testdb():
    result = data.find_one({"_id":"user46"})
    assert result["history"][0][0] == "vaccines"
    assert result["history"][0][1] == "legislation"
    assert result["history"][0][2] == "conspiracy"
    assert result["history"][0][3] == "foreign affairs"
    