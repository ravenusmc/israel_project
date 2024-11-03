<template>
    <div>
        <div ref="TypeofInjuryGraph"></div>
        graph 
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters, } from "vuex";

export default {
    name: "TypeOfInjuryGraph",
    computed: {
    ...mapGetters("datapage", [
      "typeOfInjuryData",
    ]),
  },
  watch: {
    typeOfInjuryData: {
      handler: "createTypeOfInjuryGraph",
      deep: true,
    },
  },
  mounted() {
    this.createTypeOfInjuryGraph();
  },
  methods: {
    createTypeOfInjuryGraph() {

    // Clear previous SVG elements
    d3.select(this.$refs.TypeofInjuryGraph).select("svg").remove();

    // Set the dimensions and margins of the graph
    const margin = { top: 50, right: 30, bottom: 50, left: 70 };
    const width = 800 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    }
  }
}

</script>