function barcreate(file_path){
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 400 - margin.left - margin.right,
    height = 350 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

  var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>Cost:</strong> <span style='color:white'>" + "$" + parseInt(d.cost) + "</span>";
  })

jQuery('#barchart').html('');
var svg = d3.select("#barchart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.call(tip);

d3.tsv("../static/res/radar_data_"+file_path+"_cost.tsv", type,function(error, data) {
    //console.log("in here");
  if (error) console.log(error);
  x.domain(data.map(function(d) { return d.name; }));
  y.domain([0, d3.max(data, function(d) { console.log(d.cost);return d.cost; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", -18)
      .attr("dy", "-11 em")
      .style("text-anchor", "end")
      .text("Cost in Dollars");

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.name); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.cost); })
      .attr("height", function(d) { return height - y(d.cost); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);
});
  function type(d) {
  d.cost = +d.cost;
  return d;
}

}