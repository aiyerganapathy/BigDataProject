function render_taxi_chart(Date_from,Date_to,weather_param){
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
//Defining svg margin and size
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
    .orient("bottom").ticks(ticks).tickFormat(d3.time.format("%d-%b"));

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.usage); });
    
// Adds the svg canvas
var svg = d3.select("#charts").append("svg").attr("class","col-xs-6")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");
//Get Data
d3.csv("data/weather_freq.csv", function(error, data1) {
 data1.forEach(function(d) {
        d.date =parseDate(d.date);
        d.usage = +d.usage;
    });
//Adding filter to data based on weather parameters and restrictions of date
    var data=data1.filter(function(d){
       if ((d.date<=Date_to) && (d.date>=Date_from) && d.wind>=weather_param["from_wind"] && d.wind<=weather_param["to_wind"] && d.temp>=weather_param["from_temp"] && d.temp<=weather_param["to_temp"] && d.visibility>=weather_param["from_visibility"] && d.visibility<=weather_param["to_visibility"]) { return true; }
    
    return false; 
  });
    //Adding d3-tip
    var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<b>Date :"+d["date"]+"</b><br/>"+"Temperature : "+(d.temp)+"</b><br/>"+"Wind : "+(d.wind)+"</b><br/>"+"Visibility : "+(d.visibility)+"<br/>"+"No of trips : "+d.usage;
  });
    svg.call(tip);
    // Define domain
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.usage; })]);

    // Add the valueline path.
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));

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