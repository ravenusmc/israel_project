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
            <option disabled value="">Please select one</option>
            <option v-for="injury in injuries" :key="injury" :value="injury">
              {{ injury }}
            </option>
          </select>
          <label for="ammo">Select Ammunition:</label>
          <select v-model="selectedAmmo">
            <option disabled value="">Please select one</option>
            <option v-for="ammo in ammunitions" :key="ammo" :value="ammo">
              {{ ammo }}
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
        };
        this.submitSelectedInjuryAndYearToServer({ payload });
      }
    },
  },
};
</script>