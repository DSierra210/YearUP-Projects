/*jslint browser:true */
"use strict";

const weatherConditions = new XMLHttpRequest();
const weatherForecast = new XMLHttpRequest();
let cObj;
let fObj;

// GET THE CONDITIONS
weatherConditions.open(
  "GET",
  "https://api.openweathermap.org/data/2.5/weather?zip=08527,us&appid=5ab180c74f8457efc49f18ceb7c4bed2&units=imperial",
  true
);
weatherConditions.responseType = "text";
weatherConditions.send(null);

weatherConditions.onload = function () {
  if (weatherConditions.status === 200) {
    cObj = JSON.parse(weatherConditions.responseText);
    //console.log(cObj);
    document.getElementById("location").innerHTML = cObj.name;
    document.getElementById("weather").innerHTML = cObj.weather[0].description;
    document.getElementById("temperature").innerHTML = cObj.main.temp;
    document.getElementById("desc").innerHTML = "Wind Speed " + cObj.wind.speed;
  }
};

// GET THE FORECARST
weatherForecast.open(
  "GET",
  "https://api.openweathermap.org/data/2.5/forecast?zip=08527,us&appid=5ab180c74f8457efc49f18ceb7c4bed2&units=imperial",
  true
);
weatherForecast.responseType = "text";
weatherForecast.send();

weatherForecast.onload = function () {
  let date_raw, iconcode, icon_path;

  if (weatherForecast.status === 200) {
    fObj = JSON.parse(weatherForecast.responseText);
    console.log(fObj);

    date_raw = fObj.list[0].dt_txt;
    date_raw = date_raw.substring(5, 11);
    document.getElementById("r1c1").innerHTML = date_raw;

    iconcode = fObj.list[0].weather[0].icon;
    icon_path = "https://openweathermap.org/img/w/" + iconcode + ".png";
    document.getElementById("r1c2").src = icon_path;
    document.getElementById("r1c3").innerHTML =
      fObj.list[0].main.temp_min + "&deg;";
    document.getElementById("r1c4").innerHTML =
      fObj.list[0].main.temp_max + "&deg;";

    date_raw = fObj.list[8].dt_txt;
    date_raw = date_raw.substring(5, 11);
    document.getElementById("r2c1").innerHTML = date_raw;

    iconcode = fObj.list[8].weather[0].icon;
    icon_path = "https://openweathermap.org/img/w/" + iconcode + ".png";
    document.getElementById("r2c2").src = icon_path;
    document.getElementById("r2c3").innerHTML =
      fObj.list[8].main.temp_min + "&deg;";
    document.getElementById("r2c4").innerHTML =
      fObj.list[8].main.temp_max + "&deg;";

    date_raw = fObj.list[16].dt_txt;
    date_raw = date_raw.substring(5, 11);
    document.getElementById("r3c1").innerHTML = date_raw;

    iconcode = fObj.list[16].weather[0].icon;
    icon_path = "https://openweathermap.org/img/w/" + iconcode + ".png";
    document.getElementById("r3c2").src = icon_path;
    document.getElementById("r3c3").innerHTML =
      fObj.list[16].main.temp_min + "&deg;";
    document.getElementById("r3c4").innerHTML =
      fObj.list[16].main.temp_max + "&deg;";
  }
};
