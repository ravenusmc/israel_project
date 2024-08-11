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


if __name__ == '__main__':
    app.run(debug=True)