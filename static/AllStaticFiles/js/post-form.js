// Show and hide create post form
let postForm;
let wrapper;
let wrapper2;
let createPostIcon;
let captionField;
let form;
let closePostForm;


const showForm = (updating = false, caption = null, pk = null) => {
    postForm = document.querySelector(".post-form");
    postForm.style.display = "flex";
    postForm.querySelector(".create-update > button").innerText = "Create"
    postForm.querySelector(".title > h3").innerHTML = "Create post <span id=\"close\"></span>";
    form = postForm.querySelector(".form");
    form.action = window.location.origin + "/create/";
    captionField = postForm.querySelector(".caption-input > textarea");
    captionField.innerText = null;
    postForm.querySelector(".content-input > input").setAttribute("required", "");


    // If form pop upped for editing
    if (updating) {
        postForm.querySelector(".content-input > input").removeAttribute("required");
        captionField.innerText = caption;
        postForm.querySelector(".title > h3").innerHTML = "Update post <span id=\"close\"></span>";
        postForm.querySelector(".create-update > button").innerText = "Update";
        form.action = window.location.origin + "/update/" + pk;
        wrapper2 = document.createElement("div");
        wrapper2.id = "wrapper2";
        wrapper2.style.zIndex = "2";
        wrapper2.classList.add("wrapper");
        document.body.prepend(wrapper2);
    } else {
        wrapper = document.createElement("div");
        wrapper.id = "wrapper";
        wrapper.classList.add("wrapper");
        document.body.prepend(wrapper);
    }

    // Close popup box
    closePostForm = postForm.querySelector("#close");
    closePostForm.addEventListener("click", () => {
        if (document.querySelector("#wrapper2")) {
            wrapper2.remove();
        } else {
            wrapper.remove();
        }
        postForm.style.display = "none";
    });
}


createPostIcon = document.querySelector(".fa-camera");
createPostIcon.addEventListener("click", () => {
    showForm();
});