let inputs = document.querySelectorAll(".input");
let submit = document.querySelector(".submit > input");
submit.addEventListener("click", e => {
    inputs.forEach(input => {
        if (!(input.value)) {
            e.preventDefault();
            input.classList.add("empty")
        }
    });
});

inputs.forEach(input => {
    input.addEventListener("focus", () => {
        if (input.classList.contains("empty")) {
            input.classList.remove("empty");
        }
    });
});