function gender_analysis(){
    //usage analysis
    usage_analysis();
    //duration analysis
    duration_analysis();

}
function usage_analysis(){
//setting margins and size for svg
var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;
//Setting ordinal scale for gender
var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);
//Setting linear scale for usage
var y = d3.scale.linear().range([height, 0]);
//Setting Axis
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10).tickFormat(d3.format("s"));
//Appending an svg
var svg = d3.select("#usage").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", 
          "translate(" + margin.left + "," + margin.top + ")");
//reading data
d3.csv("data/gender.csv", function(error, data) {
    
    data.forEach(function(d) {
        d.gender = d.gender;
        d.usage = +d.usage;
    });
    //defining domain for x and y axis
  x.domain(data.map(function(d) { return d.gender; }));
  y.domain([0, d3.max(data, function(d) { return d.usage; })]);
//Appending X axis and Y axis to svg
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-90)" );

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Number of trips");
//Appending bar graph to svg
  svg.selectAll("bar")
      .data(data)
    .enter().append("rect")
      .style("fill", "steelblue")
      .attr("x", function(d) { return x(d.gender); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.usage); })
      .attr("height", function(d) { return height - y(d.usage); });

});
}
function duration_analysis(){
    //defining margins for duration analysis svg
var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;


//Defining ordinal scale for gender
var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);
//Defining lnear scale for duration
var y = d3.scale.linear().range([height, 0]);
//Defining axis
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);
//Appending svg
var svg = d3.select("#duration").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", 
          "translate(" + margin.left + "," + margin.top + ")");
//Reading data
d3.csv("data/gender.csv", function(error, data) {

    data.forEach(function(d) {
        d.gender = d.gender;
        d.duration = parseFloat(d.duration);
    });
	//Defining domain
  x.domain(data.map(function(d) { return d.gender; }));
  y.domain([0, d3.max(data, function(d) { return d.duration; })]);
//Appending X and Y axis to svg
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", "-.55em")
      .attr("transform", "rotate(-90)" );

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Avg. usage time (min)");
//Appending bar graphs to svg
  svg.selectAll("bar")
      .data(data)
    .enter().append("rect")
      .style("fill", "steelblue")
      .attr("x", function(d) { return x(d.gender); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.duration); })
      .attr("height", function(d) { return height - y(d.duration); });

});
}