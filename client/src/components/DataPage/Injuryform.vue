<template>
    <div>
      <div class='form-div'>
        <form>
          <div>
            <label for="year">Enter Year:</label>
            <input v-model="year" />
          </div>
          <div class="form-group">
            <button class='styled-button' type="button" @click="submitSelectedYear">Submit</button>
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
      selectedInjury: 'gunfire',
      injuries: ['gunfire', 'stabbing', 'hit by a vehicle', 'explosion', 'physical assault', 
        'shelling', 'being bludgeoned with an axe', 'physically assaulted', 'beating', 
        'stones throwing', 'Strangulation', 'fire', 'house demolition']
    };
  },
  methods: {
    ...mapActions("datapage", ["submitSelectedYearToServer"]),
    submitSelectedYear() {
      event.preventDefault();
      if (this.year < 2000) {
        alert("Please Select a year greater than or equal to 2000");
      } else if (this.year > 2023) {
        alert("Please Select a Year Less than or equal to 2023");
      } else {
        const payload = {
          year: this.year,
        };
        this.submitSelectedYearToServer({ payload });
      }
    },
  },
};
</script>