<template>
    <div>
        <div ref="TypeofInjuryGraph"></div> 
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
      handler: "createInjuryTypePieChart",
      deep: true,
    },
  },
  mounted() {
    this.createInjuryTypePieChart();
  },
  methods: {
    createInjuryTypePieChart() {
      
      // Clear previous SVG elements
      d3.select(this.$refs.TypeofInjuryGraph).select("svg").remove();

      // Set the dimensions and radius of the pie chart
      const width = 460;
      const height = 400;
      const radius = Math.min(width, height) / 2 - 40;

    // Append the svg object to the div with id "AverageAge"
    const svg = d3
      .select(this.$refs.TypeofInjuryGraph)
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", `translate(${width / 2}, ${height / 2})`);

    // Create a color scale
    const color = d3.scaleOrdinal()
      .domain(["Palestinian Count", "Israeli Count"])
      .range(["#0B90CA", "#FF5733"]); // Colors for each category

    // Process data for the pie chart
    // const data = { "Palestinian Count": 9408, "Israeli Count": 438 };
    const data = this.typeOfInjuryData;

    // Generate the pie chart data
    const pie = d3.pie()
      .value(d => d[1]);

    const data_ready = pie(Object.entries(data));

    // Generate the arcs
    const arc = d3.arc()
      .innerRadius(0)
      .outerRadius(radius);
    
    console.log('here')
    console.log(this.typeOfInjuryData)

    // Create a tooltip
    const tooltip = d3
      .select(this.$refs.TypeofInjuryGraph)
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "white")
      .style("border", "solid")
      .style("border-width", "1px")
      .style("border-radius", "5px")
      .style("padding", "10px")
      .style("position", "absolute");

    // Tooltip functions
    const showTooltip = (event, d) => {
      tooltip
        .style("opacity", 1)
        .html(`Type: ${d.data[0]}<br>Count: ${d.data[1]}`)
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 10 + "px");
    };

    const moveTooltip = (event) => {
      tooltip
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 10 + "px");
    };

    const hideTooltip = () => {
      tooltip.style("opacity", 0);
    };

    // Draw the pie slices
    svg
      .selectAll("path")
      .data(data_ready)
      .enter()
      .append("path")
      .attr("d", arc)
      .attr("fill", d => color(d.data[0]))
      .attr("stroke", "white")
      .style("stroke-width", "2px")
      .on("mouseover", showTooltip)
      .on("mousemove", moveTooltip)
      .on("mouseleave", hideTooltip);

    // Add title
    svg
      .append("text")
      .attr("text-anchor", "middle")
      .attr("y", -height / 2 + 20) // Adjust y position for the title
      .attr("font-size", "16px")
      .attr("font-weight", "bold")
      .text("Distribution of Injury Types");
    
    }
  }
}

</script>