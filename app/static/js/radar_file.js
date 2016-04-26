/**
 * Created by Nihal on 4/24/16.
 */

function foo(file_path){
    if (file_path == "total"){
        document.getElementById("title").innerHTML = "All Meals";
    }
    else{
        document.getElementById("title").innerHTML = file_path;
    }

    var margin = {top: 100, right: 100, bottom: 100, left: 100},
				legendPosition = {x: 25, y: 25},
				width = Math.min(1000, window.innerWidth - 10) - margin.left - margin.right,
				height = Math.min(width, window.innerHeight - margin.top - margin.bottom - 20);

			//////////////////////////////////////////////////////////////
			//////////////////// Draw the Chart //////////////////////////
			//////////////////////////////////////////////////////////////

			var color = d3.scale.ordinal()
				.range(["#7CDB39","#FFE100","#FF3529","#B21AE8","#00DFFC","#93D92D", "#B0495F","#0010B0"]);

			var radarChartOptions = {
			  w: width,
			  h: height,
			  margin: margin,
			  legendPosition: legendPosition,
			  maxValue: 0.1,
			  wrapWidth: 60,
			  levels: 5,
			  roundStrokes: true,
			  color: color,
			  axisName: "reason",
			  areaName: "device",
			  value: "value",
				food: "best_food",
				sortAreas:false
			};

			//Load the data and Call function to draw the Radar chart
			d3.json("../static/res/radar_data_"+file_path+".json", function(error, data){
				RadarChart(".radarChart", data, radarChartOptions);
			});
}