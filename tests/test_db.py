from flask import Flask
from flask_pymongo import pymongo
import pytest

CONNECTION_STRING = "mongodb+srv://polygraph:polygraph#123@cluster0.w5ydh5i.mongodb.net/?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(CONNECTION_STRING)
db = cluster["test"]
test_collection = pymongo.collection.Collection(db, "test_collection")

# def add_test_data():
#     topics = ["vaccines", "legislation", "conspiracy", "foreign affairs", "pseudoscience", "COVID-19", "election fraud"]
#     for i in range(100):
#         post = {"_id": "user" + str(i), "history": [topics[i % len(topics)]]}
#         #test_collection.insert_one(post)

# add_test_data()

# def test_retrieve_history():
#     # in the future this will test retrieving actual history calling a method in db.py
#     results = test_collection.find_one({"_id":"user1"})
#     assert results[0]["history"] == "legislation"
#     results = test_collection.find({"history":"vaccines"})
#     i = 1
#     for result in results:
#         assert result["_id"] == "user" + str(i * 7)
#         i += 1