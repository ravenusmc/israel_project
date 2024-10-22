from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I made:
from data import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# route to set up new user
@app.route('/getDataForGraphs', methods=['GET', 'POST'])
def getDataForGraphs():
    if request.method == 'POST':
        data_dictionary = {}
        get_data_object = ExamineData()
        post_data = request.get_json()
        year = int(post_data['year'])
        average_age_data = get_data_object.average_age_deaths(year)
        data_dictionary['average_age_data'] = average_age_data
        print(data_dictionary)
        return jsonify(data_dictionary)


if __name__ == '__main__':
    app.run(debug=True)