# From Django
from django.urls import path

# From Apps
from . import views

app_name = "user"
urlpatterns = [
    path('register/', views.Register.as_view(), name="register"),
    path('update-profile/<int:pk>', views.EditProfile.as_view(), name="update-profile"),
    path("follow_unfollow/<username>/", views.follow_unfollow, name="follow_unfollow"),
    path("api/following/<username>/", views.following_json, name="following_json"),
]
