"use strict"

console.log('starting ui.js!')

const workers_btn = document.getElementById('workers-btn')
const projects_btn = document.getElementById('projects-btn')

workers_btn.addEventListener('click',function(){

    console.log('clicked workers-btn!')

    projects_btn.classList.remove('active-nav-btn')
    workers_btn.classList.add('active-nav-btn')
})

projects_btn.addEventListener('click',function(){

    console.log('clicked projects-btn!')

    workers_btn.classList.remove('active-nav-btn')
    projects_btn.classList.add('active-nav-btn')
})
