import os
import certifi
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://" + str(os.environ.get("DATABASE_USERNAME"))\
+ ":" + str(os.environ.get("DATABASE_PASSWORD"))\
+ "@cluster0.w5ydh5i.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
db = client.get_database('Cluster0')
user_collection = pymongo.collection.Collection(db, 'user_collection')

def add_user(user_id):
    """Adds a new user to the database
    user_id -- the id to be associated with this user for all future DB use
    returns -- True upon successful addition, and False if the user_id passed
    is already in use
    """
    if (user_collection.find_one({'user_id':user_id})):
        return False
    user_collection.insert_one({'user_id':user_id, 'history':[]})
    return True


def delete_user(user_id):
    """Deletes a user and all of its data from the database
    user_id -- the id associated with the user to be deleted
    returns -- True upon successful deletion, and False if the user was not found
    and the delete failed"""
    if (not user_collection.find_one({"user_id":user_id})):
        return False
    user_collection.delete_one({"user_id":user_id})
    return True


def get_user_history(user_id):
    """Retrieves a user's history data
    user_id: -- the associated id of the user that was assigned when the user was added
    returns -- an array of pairs, with the first element of each pair being the user's
    query and the second element being the result from that query. Will return an empty
    array if the user has no history or if the user does not exist"""
    user = user_collection.find_one({"user_id":user_id})
    if user:
        return user["history"]
    else:
        return []


def add_user_history(user_id, query, result):
    """Inserts a new entry into a user's history data
    user_id -- the associated id of the user that was assigned when the user was added
    query -- the user's text input as a string
    result -- what the program returned from the user's input as a string
    returns -- True if insertion was successful, and false if the user_id was not found
    and the insertion failed"""
    user = user_collection.find_one({"user_id":user_id})
    if not user:
        return False
    user_collection.update_one({"user_id":user_id}, {"$addToSet":{"history":[query, result]}})
    return True