"use strict";
console.log("starting ui.js!");


// highlight individual tab buttons in content card
const workers_btn = document.getElementById("workers-btn");
const projects_btn = document.getElementById("projects-btn");

// initial tab highlight
workers_btn.classList.add("active-nav-btn");

// toggle highlight
workers_btn.addEventListener("click", function () {
  console.log("clicked workers-btn!");

  projects_btn.classList.remove("active-nav-btn");
  workers_btn.classList.add("active-nav-btn");
});

projects_btn.addEventListener("click", function () {
  console.log("clicked projects-btn!");

  workers_btn.classList.remove("active-nav-btn");
  projects_btn.classList.add("active-nav-btn");
});

// websocket for notifications
//const roomGuid = '8c5eae9a-0455-440a-a15f-13164084c32e'
//const ws = new WebSocket(
//  'ws://' + window.location.host + '/dashboard/' + roomGuid +'/'
//)
//
//ws.onopen = function(){
//  console.log('websocket connected!')
//}
//ws.onclose = function(){
//  console.log('websocket disconnected!')
//}
