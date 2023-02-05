from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import requests
from flask import Response

# ...

app = Flask(__name__)
@app.route('/')
def flask_mongodb_atlas():
    return Response("Polygraph Backend & flask mongodb atlas!", status=200)
if __name__ == '__main__':
    app.run(port=8000)

import db
#test to insert data to the data base
@app.route("/test")
def test():
    db.user_collection.insert_one({"name": "test"})
    return "Connected to the data base!"

# misinformation endpoint
# raw text will be provided in request ody (req_data)
# eventually, req_data will be passed to the misinformation detection model
@app.route("/misinformation", methods=["POST"])
def parse_request():
    req_data = request.get_json()
    print(req_data)
    return Response("JSON posted", 200)