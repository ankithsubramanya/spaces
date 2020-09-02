from flask import Flask, render_template
import requests as request
import json as json

import lister_db
import space_db
import user_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Welcome to spaces backend. For documentation, go to the github page"


@app.route('/user/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def user_crud():
    json_object = json.loads(request.body)
    email = json_object['email']
    if request.method == 'GET':
        return user_db.find_user_by_email(email)

    elif request.method == 'POST':
        return user_db.add_user(json_object);

    elif request.method == 'UPDATE':
        return user_db.update_user_by_email(email, json_object);

    elif request.method == 'DELETE':
        return user_db.delete_user_by_email(email)


@app.route('/lister/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def lister_crud():
    json_object = json.loads(request.body)
    email = json_object['email']
    if request.method == 'GET':
        return lister_db.find_lister_by_email(email)

    elif request.method == 'POST':
        return lister_db.add_lister(json_object);

    elif request.method == 'UPDATE':
        return lister_db.update_lister_by_email(email, json_object);

    elif request.method == 'DELETE':
        return lister_db.delete_lister_by_email(email)


@app.route('/space/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def space_crud():
    json_object = json.loads(request.body)
    space_id = json_object['space_id']
    if request.method == 'GET':
        return space_db.find_space_by_space_id(space_id)

    elif request.method == 'POST':
        return space_db.add_space(json_object);

    elif request.method == 'UPDATE':
        return space_db.update_space_by_space_id(space_id, json_object);

    elif request.method == 'DELETE':
        return space_db.delete_space_by_space_id(space_id)



if __name__ == '__main__':
    app.run()
