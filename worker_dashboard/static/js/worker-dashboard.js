"use strict";
console.log("running worker-dashboard.js!");

// content card header tags
const chatsTag = document.getElementById("chats-tag");
const projectsTag = document.getElementById("projects-tag");

// initial tag state
chatsTag.classList.add("active-tag");
// on click
chatsTag.addEventListener("click", (e) => {
  chatsTag.classList.add("active-tag");
  projectsTag.classList.remove("active-tag");
});
projectsTag.addEventListener("click", (e) => {
  projectsTag.classList.add("active-tag");
  chatsTag.classList.remove("active-tag");
});
