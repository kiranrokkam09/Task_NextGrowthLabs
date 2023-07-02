const btons = document.querySelectorAll(".side-item");
const content = document.querySelectorAll(".text");
btons.forEach((btn) => {
    btn.addEventListener("click", () => {
        content.forEach((text) => {
            if (btn.classList.contains(text.id)) {
                console.log(text.id);
                text.style.display = "block";
            }
            else {
                text.style.display = "none";
            }
        })
    })
})