// JavaScript for event and content management for Sandhill Biome page

function getSandhillWeather(){

	let weather = "temp";

	const getTimelineURL = "https://api.tomorrow.io/v4/timelines";

	const apikey = "XQi7VX8xGL3waqWqXgz1sLSg6HU7xHbQ";

	const fields = ["temperature","windSpeed"];

	const timesteps = ["current"];

	const units = "imperial";

	const location = "37.032,-122.110"

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




function sandhillInit(){

	$("#buckwheat-div").hide(20);
	$("#rat-div").hide(20);
	$("#manzanita-div").hide(20);
	$("#spineflower-div").hide(20);

	getSandhillWeather();

};

function introHide(){

	$("#intro-div").hide(800);

};


function buckwheatShow(){

	$("#buckwheat-div").show(800);

};

//

function buckwheatHide(){

	$("#buckwheat-div").hide(800);

};

//

function ratShow(){

	$("#rat-div").show(800);

};

//

function ratHide(){

	$("#rat-div").hide(800);

};

//

function manzanitaShow(){

	$("#manzanita-div").show(800);

};

//

function manzanitaHide(){

	$("#manzanita-div").hide(800);

};

//

function spineflowerShow(){

	$("#spineflower-div").show(800);

};

function spineflowerHide(){

	$("#spineflower-div").hide(800);

};

//

$("#buckwheat-map").hover(buckwheatShow,buckwheatHide);

$("#rat-map").hover(ratShow,ratHide);

$("#manzanita-map").hover(manzanitaShow,manzanitaHide);

$("#spineflower-map").hover(spineflowerShow,spineflowerHide);




