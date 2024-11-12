<template>
    <div>
        <div ref="WhatKilledGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters, } from "vuex";

export default {
  name: "WhatKilledGraph",
  computed: {
    ...mapGetters("datapage", [
      "killedByData",
    ]),
  },
  watch: {
    killedByData: {
      handler: "createWhatKilledGraph",
      deep: true,
    },
  },
  mounted() {
    this.createWhatKilledGraph();
  },
  methods: {
    createWhatKilledGraph() {
      // Clear previous SVG elements
      d3.select(this.$refs.WhatKilledGraph).select("svg").remove();

      const width = 460;
      const height = 400;
      const radius = Math.min(width, height) / 2 - 40;

      const svg = d3
        .select(this.$refs.WhatKilledGraph)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${width / 2}, ${height / 2})`);

      const color = d3.scaleOrdinal()
        .domain(["Palestinian Count", "Israeli Count"])
        .range(["#0B90CA", "#FF5733"]);

      const data = this.killedByData;

      const pie = d3.pie().value(d => d[1]);
      const data_ready = pie(Object.entries(data));

      const arc = d3.arc()
        .innerRadius(0)
        .outerRadius(radius);

      const tooltip = d3
        .select(this.$refs.WhatKilledGraph)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("position", "absolute");

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

      // Bind data and create/update pie slices
      const path = svg
        .selectAll("path")
        .data(data_ready, d => d.data[0]);

      // Remove old elements
      path.exit().remove();

      // Append new elements with transition
      path
        .enter()
        .append("path")
        .attr("fill", d => color(d.data[0]))
        .attr("stroke", "white")
        .style("stroke-width", "2px")
        .attr("d", arc)
        .each(function(d) { this._current = d; }) // Save initial state for transition
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip)
        .transition()
        .duration(2000)
        .attrTween("d", function(d) {
          const i = d3.interpolate(this._current, d);
          this._current = i(0);
          return t => arc(i(t));
        });

      // Update existing elements with transition
      path
        .transition()
        .duration(1500)
        .attrTween("d", function(d) {
          const i = d3.interpolate(this._current, d);
          this._current = i(0);
          return t => arc(i(t));
        })
        .attr("fill", d => color(d.data[0]));

      // Add a title
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("y", -height / 2 + 20)
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Injury Type");

      // Legend
      const legend = svg
        .append("g")
        .attr("transform", `translate(${-(width / 2 - 10)}, ${height / 2 - 50})`);

      const categories = ["Palestinian Count", "Israeli Count"];
      categories.forEach((category, i) => {
        legend
          .append("rect")
          .attr("x", 10)
          .attr("y", i * 20)
          .attr("width", 18)
          .attr("height", 18)
          .style("fill", color(category));

        legend
          .append("text")
          .attr("x", 35)
          .attr("y", i * 20 + 13)
          .text(category)
          .style("font-size", "14px")
          .attr("alignment-baseline", "middle");
      });
    }
  }
}

</script>