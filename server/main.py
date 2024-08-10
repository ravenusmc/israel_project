from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I made:
from data import *
from db import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# route to set up new user
@app.route('/setUpUser', methods=['GET', 'POST'])
def setUpUser():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(post_data, hashed)
        return jsonify('5')

# Route to login in new user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        email = post_data['email']
        password = post_data['password']
        login_values = {}
        # Checking to see if the user is in the database
        login_flag, not_found, password_no_match, user = db.verify_user(
            email, password)
        login_values['login_flag'] = login_flag
        login_values['Not_found'] = not_found
        login_values['Password_no_match'] = password_no_match
        login_values['user'] = user
    return jsonify(login_values)

if __name__ == '__main__':
    app.run(debug=True)