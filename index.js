const form = document.getElementById("form");
const submitBtn = document.getElementById("submit-btn");
const loader = document.getElementById("loader");
const resultContainer = document.getElementById("result-container");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const url = document.getElementById("url").value;
  if (!url) return;

  submitBtn.disabled = true;
  loader.style.display = "block";

  fetch("/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `url=${encodeURIComponent(url)}`,
  })
    .then((response) => response.json())
    .then((data) => {
      submitBtn.disabled = false;
      loader.style.display = "none";
      resultContainer.innerHTML = JSON.stringify(data, null, 2);
      resultContainer.style.display = "block";
    })
    .catch((error) => {
      submitBtn.disabled = false;
      loader.style.display = "none";
      console.error(error);
    });
});
