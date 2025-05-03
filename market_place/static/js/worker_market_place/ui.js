"use strict";

console.log("ui running!");

let view_profile_btn = Array.from(
  document.getElementsByClassName("view-profile-btn"),
);

view_profile_btn.forEach((e) => {
  e.addEventListener("click", function () {
    console.log("clicked!");

    user_profile.style.visibility = "visible";
  });
});
