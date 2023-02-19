from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

import firebase_admin
import pyrebase
import json
from firebase_admin import credentials, auth

# ...

app = Flask(__name__)

def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    return wrap

#Connect to firebase
cred = credentials.Certificate('fbAdminConfig.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))
#Data source
users = [{'uid': 1, 'name': 'Noah Schairer'}]
#Api route to get users
@app.route('/api/userinfo')
def userinfo():
    return {'data': users}, 200
#Api route to sign up a new user
@app.route('/api/signup')
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return {'message': 'Error missing email or password'},400
    try:
        user = auth.create_user(
               email=email,
               password=password
        )
        return {'message': f'Successfully created user {user.uid}'},200
    except:
        return {'message': 'Error creating user'},400
#Api route to get a new token for a valid user
@app.route('/api/token')
def token():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except:
        return {'message': 'There was an error logging in'},400
        
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def flask_mongodb_atlas():
    return "Polygraph Backend & flask mongodb atlas!"
if __name__ == '__main__':
    app.run(port=8000)

import db
#test to insert data to the data base
@app.route("/test")
def test():
    db.user_collection.insert_one({"name": "test"})
    return "Connected to the data base! [FINALLY]" 


users = [{'uid': 1, 'name': 'Noah Schairer'}]
@app.route('/api/userinfo')
@check_token
def userinfo():
    return {'data': users}, 200
if __name__ == '__main__':
    app.run(debug=True)