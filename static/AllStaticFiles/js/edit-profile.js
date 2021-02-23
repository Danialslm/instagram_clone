let editProfilePopup;
let editProfileBtn;
let closeEditProfileForm;
let bio;
let Username;

editProfileBtn = document.querySelector(".edit-profile > button");
editProfileBtn.addEventListener("click", () => {
    // Show popup box and wrapper
    editProfilePopup = document.querySelector(".edit-profile-popup");
    wrapper = document.createElement("div");
    wrapper.id = "wrapper";
    wrapper.classList.add("wrapper");
    document.body.prepend(wrapper);
    editProfilePopup.style.display = "flex";


    Username = document.querySelector(".username > h1");
    editProfilePopup.querySelector(".username-input > input").value = Username.innerText;
    bio = document.querySelector(".biography > span");
    if (bio.innerText == "None") {
        bio.innerText = null;
    }
    editProfilePopup.querySelector(".bio-input > textarea").innerText = bio.innerText;
    pk = editProfileBtn.dataset.pk;
    form = editProfilePopup.querySelector(".form");

    form.action = window.location.origin + "/update-profile/" + pk;

    // Close popup box
    closeEditProfileForm = editProfilePopup.querySelector(".title > h3 > #close");
    closeEditProfileForm.addEventListener("click", () => {
        wrapper.remove();
        editProfilePopup.style.display = null;
    });
});