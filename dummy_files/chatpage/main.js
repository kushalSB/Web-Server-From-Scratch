const inputBox = document.getElementById("input-box");
const sendMessage = document.getElementById("send-message");
const displayBox = document.getElementById("chat-display");
const clientInputName = document.getElementById("client-name");
const submitName = document.getElementById("set-name");

const clientName = "";
submitName.addEventListener("click", setName);
sendMessage.addEventListener("click", sendRequest);

function sendRequest() {
  clientName = clientInputName.value;
}
function sendRequest() {
  fetch("http://192.168.1.72:8000/api", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: inputBox.value, name: clientName }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Response", data);
      const li = document.createElement("li");
      li.innerHTML = data["data"];
      displayBox.appendChild(li);
    })
    .catch((error) => {
      console.log("Error");
    });
}
