// Show post detail in own page or user's page when clicked on it
let pk;
let detailPostPopUp;
let posts;
let likeDislikeBtns;
let clickedPost;
let caption;
let image;
let closePopUpBtns;
let editPostBtns;
let deletePostBtns;

posts = document.querySelectorAll(".post");
posts.forEach(post => {
    post.addEventListener("click", () => {
        // Show popup box and add wrapper
        detailPostPopUp = document.querySelector(".detail-popup");
        wrapper = document.createElement("div");
        wrapper.id = "wrapper";
        wrapper.classList.add("wrapper");
        document.body.prepend(wrapper);
        detailPostPopUp.style.display = "flex";

        clickedPost = post.querySelector("img");
        pk = clickedPost.dataset.pk


        caption = detailPostPopUp.querySelectorAll(".caption > span");
        image = detailPostPopUp.querySelectorAll(".image > img");
        likeDislikeBtns = detailPostPopUp.querySelectorAll(".like-dislike");
        for (let i = 0; i < 2; i++) {
            image[i].src = clickedPost.src;
            caption[i].innerText = clickedPost.alt;
            likeDislikeBtns[i].dataset.href = clickedPost.dataset.href;
            likeDislikeBtns[i].dataset.phref = clickedPost.dataset.phref;

            // Ajax to get like count
            $.ajax({
                url: likeDislikeBtns[i].dataset.phref,
                success: () => changeHeartClass(likeDislikeBtns[i]),
                error: error => console.error(error)
            });
        }


        // Close popup box
        closePopUpBtns = detailPostPopUp.querySelectorAll("#close");
        closePopUpBtns.forEach(closePopUp => {
            closePopUp.addEventListener("click", () => {
                detailPostPopUp.style.display = null;
                wrapper.remove();
            });
        })
    });
});


// Edit post
editPostBtns = document.querySelectorAll("#edit-post");
editPostBtns.forEach(editPostBtn => {
    editPostBtn.addEventListener("click", () => {
        caption = document.querySelector(".caption > span").innerText;
        showForm(updating = true, caption = caption, pk = pk);
    });
});


// Delete post
deletePostBtns = document.querySelectorAll("#delete-post");
deletePostBtns.forEach(deletePostBtn => {
    deletePostBtn.addEventListener("click", () => {
        showDeleteForm(pk = pk)
    });
});