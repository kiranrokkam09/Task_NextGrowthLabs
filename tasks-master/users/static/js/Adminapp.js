const home = document.querySelector("#home");
const app = document.querySelector("#AddApp");
const form = document.querySelector("form");
const file = document.querySelector(".home");
app.addEventListener("click", () => {
    form.style.display = "block";
    file.style.display = "none";
})
home.addEventListener("click", () => {
    file.style.display = "block";
    form.style.display = "none";
})
