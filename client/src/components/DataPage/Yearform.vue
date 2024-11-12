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
  min-height: 10vh;
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

/* Input field */
input[type="text"] {
  width: 100%;
  padding: 8px 10px;
  margin-bottom: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.95rem;
  color: #333;
}

input[type="text"]:focus {
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
  margin-top: 15px;
}

.styled-button:hover {
  background-color: #0056b3;
}

.styled-button:focus {
  outline: none;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}
</style>

  