function render_max_usage_station(Date_from,Date_to){
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 700 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%d-%b-%Y").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.ordinal().rangeRoundBands([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5).tickFormat(d3.time.format("%d-%b-%Y"));

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line

    
// Adds the svg canvas
var svg = d3.select("#peakstation")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("max_used_station.csv", function(error, data1) {
    data1.forEach(function(d) {
        d.date = parseDate(d.date);
        d.station = d.station;
        d.usage=+d.usage;
    });
    var data=data1.filter(function(d){
       //console.log(d.date);
        //console.log(Date_from);
      if ((d.date<=Date_to) && (d.date>=Date_from)) { return true; }
    
    return false; 
  });

    var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<b>Date :"+d["date"]+"</b><br/>"+"Station : "+(d.station)+"<br/>"+"No of trips : "+d.usage;
  });
    svg.call(tip);

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain(data.map(function(d) { return d.station; }));

    // Add the valueline path.
   

    // Add the scatterplot
    svg.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.date); })
        .attr("cy", function(d) { return y(d.station); })
    .on('mouseover', tip.show)
      .on('mouseout', tip.hide);


    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

});
}