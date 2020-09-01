from flask import Flask, render_template
import requests as request
import json as json
import database

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Welcome to spaces backend, for reference, check out the github page"


@app.route('/user/', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def user_crud():
    json_object = json.loads(request.body)
    email = json_object.email
    if request.method == 'GET':
        return database.find_user_by_email(email)

    elif request.method == 'POST':
        return database.add_user(json_object);

    elif request.method == 'UPDATE':
        return database.update_user_by_email(email, json_object);

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


if __name__ == '__main__':
    app.run()
