const btns = document.querySelectorAll(".side-item");
document.addEventListener("DOMContentLoaded", () => {
    btns.forEach(btn => {
        btn.addEventListener("click", () => {
            btns.forEach((btn1) => {
                if (btn1 != btn) {
                    btn1.classList.remove("active");
                }
            })
            btn.classList.add("active");
            document.body.classList.remove('close-overflow');
            document.body.classList.remove('close-horoverflow');
            if (btn.classList.contains("Home") || btn.classList.contains("Task")) {
                document.body.classList.add("close-horoverflow");
            }
            else {
                document.body.classList.add("close-overflow");
            }
        })
    })
    var nav = document.querySelector(".sidenav");
    var body = document.body;
    var html = document.documentElement;

    var height = Math.max(body.scrollHeight, body.offsetHeight,
        html.clientHeight, html.scrollHeight, html.offsetHeight);
    nav.style.height = height + "px";
})
console.log("hi");
// let a = fetch("http://127.0.0.1:8000/api/allapps?format=json");
// a.then((response1) => {
//     return response1.json();
// }).then((response2) => {
//     console.log(response2);
// })

const file = document.querySelector(".home");

appret();
async function appret() {
    let link = new URL(`http://127.0.0.1:8000/api/allapps`);
    const response = await fetch(link);
    const data = await response.json();
    console.log(data);
    displayitems(data);
}

function displayitems(data) {
    let displayMenu = data.map(function (item) {
        return `<div class="card file" style="background-color: #DFE6ED">
        <div class="card-body">
            <div class="row">
                <div class="col">
                    <div class="col box1">
                        <img src="https://cdn.pixabay.com/photo/2016/11/18/11/16/facebook-1834007_1280.png" alt="" class="file-image">
                    </div>
                    <div class="col box1">
                        <h4>${item.name}</h4>
                        <a href="#">
                            <h6>View in Detail></h6>
                        </a>
                    </div>
                </div>
                <div class="col">
                    <div class="row points">
                        <h6>${item.points} Points</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>`
    })
    displayMenu = displayMenu.join("");
    file.innerHTML = displayMenu;
}