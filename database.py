import json
import pymongo
from pymongo import MongoClient

import Constants

# Fast facts
# 1. db returns actual JSON objects, so no need to parse


def get_db():
    client = MongoClient(Constants.mongoClientURL)
    db = client.spaces
    return db


# util

def get_user_id_from_email(email_id):
    json_object = (find_user_by_email(email_id))
    return json_object['_id']


def email_exists(email_id):
    json_object = (find_user_by_email(email_id))
    return json_object is not None


# CORE app requests - most frequently used in app flow

def find_user_by_email(email_id):
    db = get_db()
    user = db.user
    json_filter = {"email": email_id}
    res = user.find_one(json_filter)
    return res


def add_user(json_object):  # Tested
    email_id = json_object["email"]
    if email_exists(email_id):  # @todo document this idiosyncrasy
        return 0

    db = get_db()
    user = db.user
    res = user.insert_one(json_object)
    return res.inserted_id  # this is the object id


def update_user_by_email(email, update_string):  # update one param at a time
    db = get_db()
    user = db.user
    user_id = get_user_id_from_email(email)
    user.update_one({"_id": user_id}, {"$set":  update_string})


def delete_user_by_email(email):  # delete many functionality can be added later if needed
    db = get_db()
    user = db.user
    user.delete_one({"email: " + email})


# Secondary requests - nice to have
# GET requests
def find_users_by_json_filter(json_filter):
    db = get_db()
    user = db.user
    res = user.find(json_filter)
    return res


print(add_user({
    "first_name": "first",
    "last_name": "user",
    "email": "firstuser@mail.com",
    "company": "firstcompany",
    "location": "Champaign"
}))

print(get_user_id_from_email("firstuser@mail.com"))

print(find_user_by_email("firstuser@mail.com"))

update_user_by_email("firstuser@mail.com", {"first_name": "hey"})

print(find_user_by_email("firstuser@mail.com"))

print(email_exists("firstuser@mail.com"))

print(email_exists("seconduser@mail.com"))

#delete_user_by_email("firstuser@mail.com")

print(email_exists("firstuser@mail.com"))