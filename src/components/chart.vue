<template>
    <div>
      <svg ref="chart"></svg>
    </div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  
  export default {
    data() {
      return {
        chartData: [{ date: "24-Apr-07", amount: 93.24 },
    { date: "25-Apr-07", amount: 95.35 },
    { date: "26-Apr-07", amount: 98.84 },
    { date: "27-Apr-07", amount: 99.92 },
    { date: "30-Apr-07", amount: 99.8 },
    { date: "1-May-07", amount: 99.47 },
    { date: "2-May-07", amount: 100.39 },
    { date: "3-May-07", amount: 100.4 },
    { date: "4-May-07", amount: 100.81 },
    { date: "7-May-07", amount: 103.92 },
    { date: "8-May-07", amount: 105.06 },
    { date: "9-May-07", amount: 106.88 },
    { date: "10-May-07", amount: 107.34 },],
        width: 800,
        height: 500
      }
    },
    mounted() {
      const svg = d3.select(this.$refs.chart)
        .attr("width", this.width)
        .attr("height", this.height);
      const g = svg.append("g");
    }
  }
  </script>
  
  
  
  
  