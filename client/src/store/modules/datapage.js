import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	year: 2023,
	yearTwo: 2023, 
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
	DeathsByRegionData: [
        ['Gaza Strip', 7664], 
        ['West Bank', 2658], 
        ['Israel', 673]
    ],
	DeathsOfPeopleInEventData: [
		['Yes', 3466], 
		['No', 4652]
	],
	typeOfInjuryData: {'Palestinian Count': 9408, 'Israeli Count': 438},
	hideInjuryGraph: false,
	typeOfAmmoData: {'Palestinain Deaths': 1385, 'Israeli Deaths': 127},
	killedByData: {'Palestinian Deaths': 9996, 'Israeli Deaths': 1},
};

const getters = {
	year: (state) => state.year,
	yearTwo: (state) => state.yearTwo,
	averageAgaData: (state) => state.averageAgaData,
	DeathsByGroupData: (state) => state.DeathsByGroupData,
	DeathsByRegionData: (state) => state.DeathsByRegionData,
	DeathsOfPeopleInEventData: (state) => state.DeathsOfPeopleInEventData,
	typeOfInjuryData: (state) => state.typeOfInjuryData,
	hideInjuryGraph: (state) => state.hideInjuryGraph,
	typeOfAmmoData: (state) => state.typeOfAmmoData,
	killedByData: (state) => state.killedByData,
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
				commit('setDeathsByRegionData', res.data['death_count_by_region'])
				commit('setDeathsOfPeopleInEventData', res.data['took_part_in_event'])
			})
			.catch((error) => {
				console.log(error);
			});
	},

	submitSelectedInjuryAndYearToServer: ({commit}, { payload }) => {
		commit('setYearTwo', payload['yearTwo'])
		const path = 'http://localhost:5000/getDataForGraphsTwo';
		axios.post(path, payload)
		.then((res) => {
      		console.log(res.data)
			if (res.data['injury_data']['Israeli Count'] === 0 && res.data['injury_data']['Palestinian Count'] === 0) {
				commit('setHideInjuryGraph', true)
			}else {
				commit('setHideInjuryGraph', false)
			}
			commit('setTypeOfInjuryData', res.data['injury_data'])
			commit('setTypeOfAmmoData', res.data['ammo_data'])
			commit('setKilledByData', res.data['killed_by_data'])
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

	setYearTwo(state, value) {
		state.yearTwo = value
	},

	setAverageAgaData(state, value) {
		state.averageAgaData = value 
	},

	setDeathsByGroupData(state, value) {
		state.DeathsByGroupData = value
	}, 

	setDeathsByRegionData(state,value) {
		state.DeathsByRegionData = value
	}, 

	setDeathsOfPeopleInEventData(state, value) {
		state.DeathsOfPeopleInEventData = value
	},

	setTypeOfInjuryData(state, value) {
		state.typeOfInjuryData = value
	},

	setHideInjuryGraph(state, value) {
		state.hideInjuryGraph = value
	},

	setTypeOfAmmoData(state, value) {
		state.typeOfAmmoData = value
	},

	setKilledByData(state, value) {
		state.killedByData = value 
	}, 
};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};