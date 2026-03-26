"use strict";
console.log("running chat.js!");

let username = document.getElementById("username").value;

// get room guid from hidden field
let roomGuid = document.getElementById("room-guid");

// create a web socket
const ws = new WebSocket(
  "ws://" + window.location.host + "/chat_room/" + roomGuid.value + "/",
);

// connection open
ws.onopen = function (e) {
  console.log(`websocket established!`);
};

// closing connection
ws.onclose = function (e) {
  console.log(`websocket closed!`);
};

// receiving message!
ws.onmessage = function (e) {
  const parsedData = JSON.parse(e.data);
  console.log(`message received! : ${parsedData.message}`);

  // client side render logic
  const msg = parsedData.message;
  const senderName = parsedData.username;
  const time = parsedData.time;

  const msgBody = document.createElement("pre");
  msgBody.setAttribute("class", "msg-body");
  msgBody.textContent = msg;

  const senderBody = document.createElement("span");
  senderBody.setAttribute("class", "sender-body");
  senderBody.innerHTML = senderName + " | " + time;

  const msgContainer = document.getElementById("msg-container");
  msgContainer.append(msgBody);
  msgContainer.append(senderBody);
};

// on click send btn
document.getElementById("send-btn").addEventListener("click", (e) => {
  // send msg via socket!
  const msgBox = document.getElementById("msg-box");
  console.log(username);

  if (msgBox.value != "") {
    ws.send(
      JSON.stringify({
        message: msgBox.value,
        username: username,
      }),
    );
  }

  msgBox.value = "";
});
