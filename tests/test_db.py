from app import app
from flask import Flask
from flask_pymongo import pymongo
import pytest

class TestDB:
    def __init__(self, cluster):
        db = cluster["test"]
        collection = db["test"]

    def test_insert_one(self):
        post = {"_id": 0, "history": []}
        self.collection.insert_one(post)

        results = self.collection.find({"_id":0})
        assert not results