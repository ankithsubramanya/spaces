import json
import pymongo
from bson import ObjectId
from pymongo import MongoClient

import Constants

# Fast facts
# 1. db returns actual JSON objects, so no need to parse


def get_db():
    client = MongoClient(Constants.mongoClientURL)
    db = client.spaces
    return db


# util

def get_lister_id_from_email(email_id):
    json_object = (find_lister_by_email(email_id))
    return json_object['_id']


def email_exists(email_id):
    json_object = (find_lister_by_email(email_id))
    return json_object is not None


# CORE app requests - most frequently used in app flow

def find_lister_by_email(email_id):
    db = get_db()
    lister = db.lister
    json_filter = {"email": email_id}
    res = lister.find_one(json_filter)
    return res


def add_lister(json_object):  # Tested
    email_id = json_object["email"]
    if email_exists(email_id):  # @todo document this idiosyncrasy
        return 0

    db = get_db()
    lister = db.lister
    res = lister.insert_one(json_object)
    return res.inserted_id  # this is the object id


def update_lister_by_email(email, update_string):  # update one param at a time
    db = get_db()
    lister = db.lister
    lister_id = get_lister_id_from_email(email)
    lister.update_one({"_id": lister_id}, {"$set":  update_string})


def delete_lister_by_email(email):  # delete many functionality can be added later if needed
    db = get_db()
    lister = db.lister
    lister_id = get_lister_id_from_email(email)
    lister.delete_one({"_id": ObjectId(lister_id)})


# Secondary requests - nice to have
# GET requests
def find_listers_by_json_filter(json_filter):
    db = get_db()
    lister = db.lister
    res = lister.find(json_filter)
    return res


print(add_lister({
    "first_name": "first",
    "last_name": "lister",
    "email": "firstlister@mail.com",
    "company": "firstcompany",
    "location": "Champaign"
}))

print(get_lister_id_from_email("firstlister@mail.com"))

print(find_lister_by_email("firstlister@mail.com"))

update_lister_by_email("firstlister@mail.com", {"first_name": "hey"})

print(find_lister_by_email("firstlister@mail.com"))

print(email_exists("firstlister@mail.com"))

print(email_exists("secondlister@mail.com"))

delete_lister_by_email("firstlister@mail.com")

print(email_exists("firstlister@mail.com"))