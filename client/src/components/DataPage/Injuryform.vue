<template>
    <div>
      <div class='form-div'>
        <form>
          <div>
            <label for="year">Enter Year:</label>
            <input v-model="yearTwo" />
          </div>
          <label for="Injury">Select Injury:</label>
          <select v-model="selectedInjury">
            <option disabled>Please select one</option>
            <option v-for="injury in injuries" :key="injury" :value="injury">
              {{ injury }}
            </option>
          </select>
          <label for="ammo">Select Ammunition:</label>
          <select v-model="selectedAmmo">
            <option disabled>Please select one</option>
            <option v-for="ammo in ammunitions" :key="ammo" :value="ammo">
              {{ ammo }}
            </option>
          </select>
          <label for="ammo">Select Group:</label>
          <select v-model="selectedKilledBy">
            <option disabled>Please select one</option>
            <option v-for="group in killedByGroups" :key="group" :value="group">
              {{ group }}
            </option>
          </select>
            <div class="form-group">
              <button class='styled-button' type="button" @click="submitInjuryAndYearToServer">Submit</button>
            </div>
        </form>
      </div>
    </div>
  </template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Injuryform",
  data() {
    return {
      yearTwo: 2023,
      selectedInjury: 'gunfire',
      injuries: ['gunfire', 'stabbing', 'hit by a vehicle', 'explosion', 'physical assault', 
        'shelling', 'being bludgeoned with an axe', 'physically assaulted', 'beating', 
        'stones throwing', 'Strangulation', 'fire', 'house demolition'],
      selectedAmmo: 'live ammunition',
      ammunitions: ['live ammunition', 'missile', 'rocket', '0.22-caliber bullets', 'bomb', 
      'knife', 'shell', 'rock', 'rubber-coated metal bullets', 'stun grenade', 
      'teargas canister', 'flare bomb', 'sponge rounds', 'mortar fire', 
      'grad rocket', 'flechette shells', 'phosphorus shell', 'Qassam rocket', 
      'explosive belt', 'grenade', 'car bomb'],
      selectedKilledBy: 'Israeli security forces',
      killedByGroups: ['Israeli security forces', 'Palestinian civilians', 'Israeli civilians'],
    };
  },
  methods: {
    ...mapActions("datapage", ["submitSelectedInjuryAndYearToServer"]),
    submitInjuryAndYearToServer() {
      event.preventDefault();
      if (this.yearTwo < 2000) {
        alert("Please Select a year greater than or equal to 2000");
      } else if (this.yearTwo > 2023) {
        alert("Please Select a Year Less than or equal to 2023");
      } else {
        const payload = {
          yearTwo: this.yearTwo,
          injury: this.selectedInjury,
          ammo: this.selectedAmmo,
          killedByGroup: this.selectedKilledBy,
        };
        this.submitSelectedInjuryAndYearToServer({ payload });
      }
    },
  },
};
</script>

<style scoped>
/* Base styles */
* {
  box-sizing: border-box;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.form-div {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 20vh;
  background-color: #f5f6fa;
}

form {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px 30px;
  max-width: 400px;
  width: 100%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Labels */
label {
  display: block;
  margin-bottom: 6px;
  font-size: 0.9rem;
  color: #333;
}

/* Input fields and selects */
input[type="text"],
select {
  width: 100%;
  padding: 8px 10px;
  margin-bottom: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.95rem;
  color: #333;
}

input[type="text"]:focus,
select:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.25);
}

/* Submit button */
.styled-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.styled-button:hover {
  background-color: #0056b3;
}

.styled-button:focus {
  outline: none;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}
</style>
