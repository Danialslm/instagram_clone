// Show and hide Submenu
$(".fa-user").click(() => {
    $(".submenu").toggleClass("show-submenu");
});

// Like Dislike
const changeHeartClass = likeDislikeJsonUrl => {
    $.ajax({
        url: likeDislikeJsonUrl.dataset.phref,
        success: data => {
            let i = likeDislikeJsonUrl.querySelector("i");
            i.classList.toggle("far", !data.is_liked);
            i.classList.toggle("fas", data.is_liked);
            let likeCount = likeDislikeJsonUrl.nextElementSibling;
            likeCount.innerHTML = `Liked <b>${data.like_count}</b>`;
        },
        error: error => console.error(error)
    });
}


const followUnfollow = followUnfollowBtn => {
    $.ajax({
        url: followUnfollowBtn.dataset.phref,
        success: (data) => {
            followUnfollowBtn.innerText = "follow";
            if (data.following) {
                followUnfollowBtn.innerText = "unfollow";
            }
        },
        error: error => console.error(error)
    });
}

const showDeleteForm = pk => {
    let deleteForm = document.querySelector(".delete-popup");
    deleteForm.style.display = "flex";
    wrapper2 = document.createElement("div");
    wrapper2.id = "wrapper2";
    wrapper2.style.zIndex = "2";
    wrapper2.classList.add("wrapper");
    document.body.prepend(wrapper2);
    let form = deleteForm.querySelector("form");
    form.action = window.location.origin + "/delete/" + pk;

    // Close popup box
    let closeDeleteForm = deleteForm.querySelector("#close");
    closeDeleteForm.addEventListener("click", () => {
        wrapper2.remove();
        deleteForm.style.display = null;
    })
}