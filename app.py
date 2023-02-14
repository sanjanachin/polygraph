import os
import openai
import json

import db

from flask import Flask, request, jsonify
from flask import Response

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
    if text == "":
        raise Exception("Request text is empty")
    return Response(text, 200)

prompt_string = "The following text contains misinformation. True or false?: "

# model response using openai direct completion
@app.route("/model", methods=["POST", "OPTIONS"])
def model_basic_req_resp():
    headers = {'Content-Type' : 'application/json; charset=utf-8',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods' : '*',
                    'Access-Control-Allow-Headers' : '*'}

    def res_to_fe_res(res):
        output = res.choices[0].text
        get_first = output.split()[0].strip(".")
        if get_first == "False":
            return Response(response=json.dumps({"valid": False}), status=200, headers=headers)
        else:
            return Response(response=json.dumps({"valid": True}), status=200, headers=headers)

    if request.method == "POST":
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
        # return text_to_bool(output).get_data()
        return res_to_fe_res(response)

    return Response(status=204, headers=headers)

if __name__ == '__main__':
    app.run(port=8000, ssl_context='adhoc')
