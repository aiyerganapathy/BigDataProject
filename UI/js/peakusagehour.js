function render_max_usage_hour(Date_from,Date_to){
//Getting difference in time between from and to date
var timeDiff = Math.abs(Date_to.getTime() - Date_from.getTime());
//Converting Time difference to day difference
var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 
//Defining number of ticks to be displayed in x axis
    var ticks=0
    if(diffDays<6){
        ticks=diffDays;
    }
    else{
        ticks=12;
    }
    //Defining margins and size of svg
    var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%d-%b-%Y").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(ticks).tickFormat(d3.time.format("%d-%b-%Y"));

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);
 
// Adds the svg canvas
var svg = d3.select("#peakusage")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("data/final_result_citi_peak.csv", function(error, data1) {
    data1.forEach(function(d) {
        
        d.date = parseDate(d.date);
        d.hour = +d.hour;
        d.count=+d.count;
    });
    //Add filter based on from and to dates
    var data=data1.filter(function(d){
      if ((d.date<=Date_to) && (d.date>=Date_from)) { return true; }
    
    return false; 
  });
    //Add d3 tip
    var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<b>Date :"+d["date"]+"</b><br/>"+"Hour : "+(d.hour)+"<br/>"+"No of trips : "+d.count;
  });
    svg.call(tip);

    // Define domain
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.hour; })]);

    // Add the scatterplot
    svg.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.date); })
        .attr("cy", function(d) { return y(d.hour); })
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