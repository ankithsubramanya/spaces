from flask import Flask, render_template
import requests as request
import json as json
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
        return "ECHO: DELETE"


if __name__ == '__main__':
    app.run()
