from flask import Flask, jsonify, request
from flask_cors import CORS

# Importing files that I made:
from data import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

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
        return jsonify(data_dictionary)

@app.route('/getDataForGraphsTwo', methods=['GET', 'POST'])
def getDataForGraphsTwo():
    if request.method == 'POST':
        data_dictionary_second_set_graphs = {}
        get_data_object = ExamineData()
        post_data = request.get_json()
        year = int(post_data['yearTwo'])
        injury = post_data['injury']
        ammo = post_data['ammo']
        killed_by = post_data['killedByGroup']
        injury_data = get_data_object.graph_of_common_injury(year, injury)
        data_dictionary_second_set_graphs['injury_data'] = injury_data
        ammo_data = get_data_object.common_ammunition_used(year, ammo)
        data_dictionary_second_set_graphs['ammo_data'] = ammo_data
        killed_by_data = get_data_object.what_killed_individual(year, killed_by)
        data_dictionary_second_set_graphs['killed_by_data'] = killed_by_data
        return jsonify(data_dictionary_second_set_graphs)


if __name__ == '__main__':
    app.run(debug=True)