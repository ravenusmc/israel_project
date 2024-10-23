import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	year: 2023,
	averageAgaData: [
        ['Israeli', 36.0],
        ['Jordanian', 33.0], 
        ['Palestinian', 26.0],
        ['American', 16.0], 
      ],
	DeathsByGroupData: [
        ['Palestinian', 9973], 
        ['Israeli', 1019], 
        ['Jordanian', 2], 
        ['American', 1]
    ],
};

const getters = {
	year: (state) => state.year,
	averageAgaData: (state) => state.averageAgaData,
	DeathsByGroupData: (state) => state.DeathsByGroupData
};

const actions = {

	submitSelectedYearToServer: ({ commit }, { payload }) => {
		commit('setYear', payload['year'])
		const path = 'http://localhost:5000/getDataForGraphs';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setAverageAgaData', res.data['average_age_data'])
				commit('setDeathsByGroupData', res.data['deaths_by_group_data'])
			})
			.catch((error) => {
				console.log(error);
			});
	},
};

const mutations = {

	setYear(state, value) {
		state.year = value;
	},

	setAverageAgaData(state, value) {
		state.averageAgaData = value 
	},

	setDeathsByGroupData(state, value) {
		state.DeathsByGroupData = value
	}, 

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};