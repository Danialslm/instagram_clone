# From Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

# From Apps
from Post.models import Post
from User.models import Contact, User

# Third party
from extentions.utils import grouper


class Explorer(LoginRequiredMixin, ListView):
    template_name = "Post/explore.html"
    queryset = Post.objects.all()


class Home(LoginRequiredMixin, ListView):
    template_name = "Post/home.html"

    # get the posts of those you following
    def get_queryset(self):
        followings = Contact.objects.filter(user_from=self.request.user)
        posts = list()
        for contact in followings:
            posts.append(Post.objects.filter(publisher=contact.user_to))
        return posts


class UserPage(LoginRequiredMixin, ListView):
    template_name = "Post/usersPage.html"

    # get user's post and group them
    def get_queryset(self):
        global user
        global objects
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        if user == self.request.user:
            self.template_name = "Post/ownPage.html"
        objects = Post.objects.filter(publisher=user)
        gp_list = list(grouper(3, objects))
        return gp_list

    # send some context to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"User": user, "post_count": objects.count()})
        return context
