<template>
    <div>
    <div id="AverageAge">Avg</div>
    </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "Avgage",
  mounted() {
    this.createGraphFive();
  },  
  methods: {
    createGraphFive() {
      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div with id "graphFive"
      let svg = d3
        .select("#AverageAge")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      let data = [
        ['American', 16.0], 
        ['Israeli', 36.0],
        ['Jordanian', 33.0], 
        ['Palestinian', 26.0]
      ]


    }
  }
}

</script>

<style scoped>
</style>


<!-- reference: 
https://github.com/ravenusmc/missing_411_project/blob/main/client/src/components/graphs/Coast.vue 

-->