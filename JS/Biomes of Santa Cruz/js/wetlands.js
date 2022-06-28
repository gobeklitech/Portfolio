// JavaScript for event and content management for Wetlands Biome page

function getWetlandsWeather(){

	let weather = "temp";

	const getTimelineURL = "https://api.tomorrow.io/v4/timelines";

	const apikey = "XQi7VX8xGL3waqWqXgz1sLSg6HU7xHbQ";

	const fields = ["temperature","windSpeed"];

	const timesteps = ["current"];

	const units = "imperial";

	const location = "36.967,-122.124"

	$.ajax({
	    
	    url: getTimelineURL,
	    
	    data: { 
	            apikey: apikey,
	            fields: fields,
	            timesteps: timesteps,
	            location: location,
	            units: units
	          },

	    type: "GET",

	    dataType : "json",

	    success: function(data) {

	        console.log("I've Succeeded!");

	        console.log(data);

	        let current_temp = data.data.timelines[0].intervals[0].values.temperature;

	        let current_wind_speed = data.data.timelines[0].intervals[0].values.windSpeed;

	        console.log("Temperature: " + current_temp);

	        console.log("Wind Speed: " + current_wind_speed);

	        $("#output-weather").append("<strong>Current Temperature: " + current_temp + " degrees Fahrenheit.</strong>");

	        $("#output-weather").append("<br><br>");

	       	$("#output-weather").append("<strong>Current Wind Speed: " + current_wind_speed + " miles per hour.</strong><br>");

	    },

	    error: function (jqXHR, textStatus, errorThrown) { 

	    	console.log("I've Failed..");

	        console.log("Error:", textStatus, errorThrown);
	    }
	})

}


function wetlandsInit(){
           
	$("#tule-div").hide(20);
	$("#waterfowl-div").hide(20);
	$("#rush-div").hide(20);
	$("#frog-div").hide(20);
	$("#willow-div").hide(20);

	getWetlandsWeather();

};


function introHide(){

	$("#intro-div").hide(800);

};


function tuleShow(){

	$("#tule-div").show(800);

};

//

function tuleHide(){

	$("#tule-div").hide(800);

};

//

function waterfowlShow(){

	$("#waterfowl-div").show(800);

};

//

function waterfowlHide(){

	$("#waterfowl-div").hide(800);

};

//

function willowShow(){

	$("#willow-div").show(800);

};

//

function willowHide(){

	$("#willow-div").hide(800);

};

//

function frogShow(){

	$("#frog-div").show(800);

};

function frogHide(){

	$("#frog-div").hide(800);

};

//

function rushShow(){

	$("#rush-div").show(800);

};

function rushHide(){

	$("#rush-div").hide(800);

};

//

$("#tule-map").hover(tuleShow,tuleHide);

$("#waterfowl-map").hover(waterfowlShow,waterfowlHide);

$("#willow-map").hover(willowShow,willowHide);

$("#frog-map").hover(frogShow,frogHide);

$("#rush-map").hover(rushShow,rushHide);



