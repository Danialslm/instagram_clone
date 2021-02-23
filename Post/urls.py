# From Django
from django.urls import path

# From Apps
from Views import views as v
from . import views

app_name = "post"
urlpatterns = [
    path("", v.Home.as_view(), name="home"),
    path("explore/", v.Explorer.as_view(), name="explore"),
    path("create/", views.CreatePost.as_view(), name="create_post"),
    path("update/<int:pk>", views.EditPost.as_view(), name="update_post"),
    path("delete/<int:pk>", views.DeletePost.as_view(), name="delete_post"),
    path("api/like_json/<int:pk>/", views.like_json, name="like_json"),
    path("api/like/<int:pk>/", views.like, name="like"),
    path("page/<username>/", v.UserPage.as_view(), name="user_page"),
]

