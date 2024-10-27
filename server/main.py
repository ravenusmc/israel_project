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
        deaths_by_group_data = get_data_object.deaths_by_group(year)
        data_dictionary['deaths_by_group_data'] = deaths_by_group_data
        death_count_by_region = get_data_object.deaths_by_region(year)
        data_dictionary['death_count_by_region'] = death_count_by_region
        took_part_in_event = get_data_object.deaths_of_people_took_part_in_event(year)
        data_dictionary['took_part_in_event'] = took_part_in_event
        # print(data_dictionary)
        return jsonify(data_dictionary)


if __name__ == '__main__':
    app.run(debug=True)