import os
import openai
import json

import db

from flask import Flask, request
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

headers = {'Content-Type' : 'application/json; charset=utf-8',
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Methods' : '*',
                'Access-Control-Allow-Headers' : '*'}

db_user_1 = "michaeljordan3"
db_user_2 = "lilamaresh"

# User history endpoint for frontend to retrieve user history
# Username is the user's email, provided in the request body
@app.route("/history", methods=["POST", "OPTIONS"])
def get_history():
    # If route is an OPTIONS from frontend, return the permission headers
    if request.method == "OPTIONS":
        return Response(status=204, headers=headers)
    user = request.get_json()["user"]
    if user == "":
        raise Exception("User email is empty")
    history = db.get_user_history(user)
    return Response(response=json.dumps({"history": history}), status=200, headers=headers)


# Frontend misinformation endpoint that will handle all of the necessary
# interactions between backend and firebase + model + db
@app.route("/misinformation", methods=["POST", "OPTIONS"])
def handle_fe_request():
    # If route is an OPTIONS from frontend, return the permission headers
    if request.method == "OPTIONS":
        return Response(status=204, headers=headers)
    # Find the user query, and raise exception if empty
    # NOTE: Parsing will be handled by frontend for future iterations
    query = request.get_json()["text"]
    if query == "":
        raise Exception("Request text is empty")

    db_user = request.get_json()["user"]
    if db_user == "":
        raise Exception("Request user not given")

    model_res = model_basic_resp(request)
    # TODO: Get user tag from firebase auth login and add to DB
    db.add_user(db_user)
    # if (size(db.get_user_history(db_user_1)) > 20):
    #     db.addAndReplace(db_user_1)
    # TODO: Introduce find and replace option for max length history
    db.add_user_history(db_user, query, str(model_res.get_json()["valid"]))
    # return the model response back to frontend
    return model_res

# Takes a request with text and outputs the truth value generated from
# running to davinci-003 with misinformation prompt_string
def model_basic_resp(request):
    prompt_string = "The following text contains misinformation. True or false?: "

    def res_to_fe_res(res):
        output = res.choices[0].text
        get_first = output.split()[0].strip(".")
        if get_first == "False":
            return Response(response=json.dumps({"valid": False}), status=200, headers=headers)
        else:
            return Response(response=json.dumps({"valid": True}), status=200, headers=headers)

    text = request.get_json()["text"]
    # a basic response pattern for davinci 003
    response = openai.Completion.create(
        model="text-davinci-003",
        # note specific prompt will be subject to change depending on test accuracy
        # will eventually integrate prompt data from frontend endpoint
        prompt=prompt_string + text,
        temperature=0.6,
        # small token size for now, will expand with greater testing
        max_tokens=500,
    )
    # return text_to_bool(output).get_data()
    return res_to_fe_res(response)

if __name__ == '__main__':
    app.run(port=8000, ssl_context='adhoc')
