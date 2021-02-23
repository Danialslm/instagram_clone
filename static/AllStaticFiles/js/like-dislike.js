// Like and dislike a post without refresh

const ajaxRequest = likeDislikeJsonUrl => {
    $.ajax({
        url: likeDislikeJsonUrl.dataset.href,
        success: () => changeHeartClass(likeDislikeJsonUrl),
        error: error => console.error(error)
    });
}


let likeDislikeJsonUrls = document.querySelectorAll(".like-dislike");
likeDislikeJsonUrls.forEach(likeDislikeJsonUrl => {
    likeDislikeJsonUrl.addEventListener("click", () => {
        ajaxRequest(likeDislikeJsonUrl);
    });
    changeHeartClass(likeDislikeJsonUrl);
});