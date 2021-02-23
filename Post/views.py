# From Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from .mixins import AccessMixin
# From Apps
from .models import Post


# Create your views here.
class CreatePost(LoginRequiredMixin, CreateView):
    # create post
    model = Post
    fields = ["content", "caption"]

    # redirect after creation post
    def get_success_url(self):
        return reverse("post:user_page", args=[self.request.user.username])

    # set publisher to self
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.publisher = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, AccessMixin, UpdateView):
    # edit post
    model = Post
    fields = ["caption", "content"]

    # redirect after editing post
    def get_success_url(self):
        return reverse("post:user_page", args=[self.request.user.username])


class DeletePost(LoginRequiredMixin, AccessMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse("post:user_page", args=[self.request.user.username])


@login_required
# will return a json of like detail
def like_json(request, pk):
    return JsonResponse({
        "like_count": get_object_or_404(Post, pk=pk).like.count(),
        "is_liked": request.user in get_object_or_404(Post, pk=pk).like.all(),
        "pk": pk
    })


@login_required
# like a post
def like(request, pk):
    Post.objects.like_dislike(request, pk=pk)
    return JsonResponse({
        "like_count": get_object_or_404(Post, pk=pk).like.count(),
        "is_liked": request.user in get_object_or_404(Post, pk=pk).like.all(),
        "pk": pk
    })
