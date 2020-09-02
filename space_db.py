import json
import pymongo
from bson import ObjectId
from pymongo import MongoClient

import Constants

# Fast facts
# 1. db returns actual JSON objects, so no need to parse
# @todo space_id is a unique id constructed by us that maps to a specific space.  "" + space_name + "@" + lister_space_id.


def get_db():
    client = MongoClient(Constants.mongoClientURL)
    db = client.spaces
    return db


# util

def get_object_id_from_space_id(space_id):
    json_object = (find_space_by_space_id(space_id))
    return json_object['_id']


def space_id_exists(space_id):
    json_object = (find_space_by_space_id(space_id))
    return json_object is not None


# CORE app requests - most frequently used in app flow

def find_space_by_space_id(space_id):
    db = get_db()
    space = db.space
    json_filter = {"space_id": space_id}
    res = space.find_one(json_filter)
    return res


def add_space(json_object):  # Tested
    space_id = json_object["space_id"]
    if space_id_exists(space_id):  # @todo document this idiosyncrasy
        return 0

    db = get_db()
    space = db.space
    res = space.insert_one(json_object)
    return res.inserted_id  # this is the object id


def update_space_by_space_id(space_id, update_string):  # update one param at a time
    db = get_db()
    space = db.space
    space_id = get_object_id_from_space_id(space_id)
    space.update_one({"_id": space_id}, {"$set":  update_string})


def delete_space_by_space_id(space_id):  # delete many functionality can be added later if needed
    db = get_db()
    space = db.space
    space_id = get_object_id_from_space_id(space_id)
    space.delete_one({"_id": ObjectId(space_id)})


# Secondary requests - nice to have
# GET requests
def find_spaces_by_json_filter(json_filter):
    db = get_db()
    space = db.space
    res = space.find(json_filter)
    return res


print(add_space({
    "first_name": "first",
    "last_name": "space",
    "space_id": "firstspace@mail.com",
    "company": "firstcompany",
    "location": "Champaign"
}))

print(get_object_id_from_space_id("firstspace@mail.com"))

print(find_space_by_space_id("firstspace@mail.com"))

update_space_by_space_id("firstspace@mail.com", {"first_name": "hey"})

print(find_space_by_space_id("firstspace@mail.com"))

print(space_id_exists("firstspace@mail.com"))

print(space_id_exists("secondspace@mail.com"))

delete_space_by_space_id("firstspace@mail.com")

print(space_id_exists("firstspace@mail.com"))