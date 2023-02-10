from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://polygraph:PASSWORD@cluster0.w5ydh5i.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Cluster0')
user_collection = pymongo.collection.Collection(db, 'user_collection')

# Adds a new user to the database
# user_id: the id to be associated with this user for all future DB use
# Returns True upon successful addition, and False if the user_id passed
# is already in use
def add_user(user_id):
    if (not user_collection.find_one({"_id":user_id})):
        return False
    user_collection.insert_one({"_id:":user_id}, {"history":[]})
    return True

# Retrieves a user's history data
# user_id: the associated id of the user that was assigned when the user was added
# returns: an array of pairs, with the first element of each pair being the user's
# query and the second element being the result from that query. Will return an empty
# array if the user has no history or if the user does not exist
def get_user_history(user_id):
    return user_collection.find_one({"_id":user_id})["history"]

# Inserts a new entry into a user's history data
# user_id: the associated id of the user that was assigned when the user was added
# query: the user's input
# result: what the program returned from the user's input
def add_user_history(user_id, query, result):
    user_collection.update_one({"_id":user_id}, {"$addToSet":{"history":[query, result]}})