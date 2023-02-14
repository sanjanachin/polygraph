import os
import db
import openai
import requests

from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient
from flask import Response

# ...

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def flask_mongodb_atlas():
    return Response("Polygraph Backend & Flask Mongodb Atlas!", status=200)

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
    text = req_data["text"]
    print(req_data)
    return Response(text, 200)

prompt_string = "The following text contains misinformation: True or false?: "

# model response using openai direct completion
@app.route("/model", methods=["POST"])
def model_basic_req_resp():

    def text_to_bool(text):
        get_first = text.split()[0].strip(".")
        if get_first == "True":
            return Response(True, 200)
        elif get_first == "False":
            return Response(False, 200)
        else:
            return Response(False, 400)

    text = request.get_json()["text"]
    # a basic response pattern for davinci 003
    response = openai.Completion.create(
        model="text-davinci-003",
        # note specific prompt will be subject to change depending on test accuracy
        # will eventually integrate prompt data from frontend endpoint
        prompt=prompt_string + text,
        temperature=0.6,
        # small token size for now, will expand with greater testing
        max_tokens=100,
    )
    # for now take the first choice with no fine-tuning
    output = response.choices[0].text
    return text_to_bool(output).get_data()

if __name__ == '__main__':
    app.run(port=8000, ssl_context='adhoc')
