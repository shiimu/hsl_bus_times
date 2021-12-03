"use strict"

window.onload = displayClock();

function displayClock(){
  let display = new Date().toLocaleTimeString();
  document.getElementById("clock").innerHTML = display;
  setTimeout(displayClock,1000)
  };



