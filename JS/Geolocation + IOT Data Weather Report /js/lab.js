// Teddy Hayden

// Wednesday, 22nd of May, 2022 

// Experimentation with AJAX via jQuery

let activatebutton = document.getElementById("activate");

let weatherbutton = document.getElementById("get-weather");


function getLocation() {

	if (navigator.geolocation) {

		navigator.geolocation.getCurrentPosition(getWeather) ;

	}	

	else {

		$("#output-geo").append("Your browser does not support location services :(");

	}

}


function getWeather(position) {

	//getLocation() ;

	let userLat = position.coords.latitude ;

	let userLon = position.coords.longitude ;

	$("#output-geo").append("Latitude: " + userLat + "<br>" + "Longitude: " + userLon + "<hr>");

	let weather = "temp";

	const getTimelineURL = "https://api.tomorrow.io/v4/timelines";

	const apikey = "XQi7VX8xGL3waqWqXgz1sLSg6HU7xHbQ";

	const fields = ["temperature","windSpeed"];

	const timesteps = ["current"];

	const units = "imperial";

	const location = userLat.toFixed(3) + "," + userLon.toFixed(3);

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

	        $("#output-weather").append("The current temperature in your location is around " + current_temp + " degrees Fahrenheit.");

	        $("#output-weather").append("<br>");

	       	$("#output-weather").append("The current wind speed in your location is around " + current_wind_speed + " miles per hour.");

	    },

	    error: function (jqXHR, textStatus, errorThrown) { 

	    	console.log("I've Failed..");

	        console.log("Error:", textStatus, errorThrown);
	    }
	})

}

activatebutton.addEventListener("click",getLocation);

