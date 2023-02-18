const inputBox = document.getElementById("input-box");
const searchButton = document.getElementById("Search-Button");
const displayBox = document.getElementById("display-box");

searchButton.addEventListener("click", sendRequest);

function sendRequest() {
  fetch("http://localhost:8000/api", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ searchQuerry: inputBox.value }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Response", data);
      displayBox.innerHTML = data["data"];
    })
    .catch((error) => {
      console.log("Error");
    });
}
