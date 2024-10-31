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

    // Append the svg object to the div
    const svg = d3
        .select(this.$refs.TypeofInjuryGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Prepare data
    const subgroups = ["firstValue", "secondValue"];
    const groups = this.typeOfInjuryData.map(d => d[0]);

    // Add X axis
    const x = d3
        .scaleBand()
        .domain(groups)
        .range([0, width])
        .padding(0.2);

    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add Y axis
    const y = d3
        .scaleLinear()
        .domain([0, d3.max(this.typeOfInjuryData.flatMap(d => [d[1], d[2]]))])
        .range([height, 0]);

    svg.append("g").call(d3.axisLeft(y));

    // Subgroup position scale
    const xSubgroup = d3
        .scaleBand()
        .domain(subgroups)
        .range([0, x.bandwidth()])
        .padding(0.05);

    // Color scale
    const color = d3.scaleOrdinal()
        .domain(subgroups)
        .range(["#0B90CA", "#CA0B0B"]);

    // Tooltip div
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
            .html("Nationality: " + d.event + "<br>Value: " + d.value)
            .style("left", event.pageX + 10 + "px")
            .style("top", event.pageY - 10 + "px");
    };

    const moveTooltip = (event, d) => {
        tooltip
            .style("left", event.pageX + 10 + "px")
            .style("top", event.pageY - 10 + "px");
    };

    const hideTooltip = () => {
        tooltip.style("opacity", 0);
    };

    // Map data for grouped bars
    const mappedData = this.typeOfInjuryData.map(d => {
        return [
            { event: d[0], value: d[1], subgroup: "firstValue" },
            { event: d[0], value: d[2], subgroup: "secondValue" }
        ];
    }).flat();

    // Add bars
    svg.append("g")
        .selectAll("g")
        .data(mappedData)
        .enter()
        .append("rect")
        .attr("x", d => x(d.event) + xSubgroup(d.subgroup))
        .attr("y", height)
        .attr("width", xSubgroup.bandwidth())
        .attr("height", 0)
        .attr("fill", d => color(d.subgroup))
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip)
        .transition()
        .duration(1500)
        .attr("y", d => y(d.value))
        .attr("height", d => height - y(d.value));

    // Add X axis label
    svg.append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Cause of Injury");

    // Add Y axis label
    svg.append("text")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Deaths");

    // Add title
    svg.append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2 + 10)
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Deaths by Type of Injury");

    }
  }
}

</script>