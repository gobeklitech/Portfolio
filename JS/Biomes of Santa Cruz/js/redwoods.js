// JavaScript for event and content management for Redwoods Biome page


function getRedwoodsWeather(){

	let weather = "temp";

	const getTimelineURL = "https://api.tomorrow.io/v4/timelines";

	const apikey = "XQi7VX8xGL3waqWqXgz1sLSg6HU7xHbQ";

	const fields = ["temperature","windSpeed"];

	const timesteps = ["current"];

	const units = "imperial";

	const location = "37.021,-122.047"

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




function redwoodsInit(){

	$("#deer-div").hide(20);
	$("#bay-div").hide(20);
	$("#coyote-div").hide(20);
	$("#foamflower-div").hide(20);
	$("#poison-oak-div").hide(20);
	$("#woodpecker-div").hide(20);

	getRedwoodsWeather();

};

function introHide(){

	$("#intro-div").hide(800);
}

function deerShow(){

	$("#deer-div").show(800);

};

//

function deerHide(){

	$("#deer-div").hide(800);

};

//

function bayShow(){

	$("#bay-div").show(800);

};

//

function bayHide(){

	$("#bay-div").hide(800);

};

//

function coyoteShow(){

	$("#coyote-div").show(800);

};

//

function coyoteHide(){

	$("#coyote-div").hide(800);

};

//

function foamflowerShow(){

	$("#foamflower-div").show(800);

};

function foamflowerHide(){

	$("#foamflower-div").hide(800);

};

//

function poisonoakShow(){

	$("#poison-oak-div").show(800);

};

function poisonoakHide(){

	$("#poison-oak-div").hide(800);

};

//

function woodpeckerShow(){

	$("#woodpecker-div").show(800);

};

function woodpeckerHide(){

	$("#woodpecker-div").hide(800);

};

//

$("#woodpecker-map").hover(woodpeckerShow,woodpeckerHide);

$("#coyote-map").hover(coyoteShow,coyoteHide);

$("#foamflower-map").hover(foamflowerShow,foamflowerHide);

$("#poison-oak-map").hover(poisonoakShow,poisonoakHide);

$("#bay-map").hover(bayShow,bayHide);

$("#deer-map").hover(deerShow,deerHide);




