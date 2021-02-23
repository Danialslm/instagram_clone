// follow and un follow without refresh
let followUnfollowBtn = document.querySelector(".follow-unfollow > button");
followUnfollow(followUnfollowBtn);
followUnfollowBtn.addEventListener("click", () => {
    $.ajax({
        url: followUnfollowBtn.dataset.href,
        success: () => {
            followUnfollow(followUnfollowBtn);
        },
        error: error => console.error(error)
    });
});