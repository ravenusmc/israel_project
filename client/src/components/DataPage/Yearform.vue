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

<!-- https://github.com/ravenusmc/missing_411_project/blob/main/client/src/components/forms/Mapform.vue -->
<script>
import { mapActions } from "vuex";

export default {
  name: "Yearform",
  data() {
    return {
      year: 2023,
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
  