# From Django
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

# From Apps
from .forms import SignUpForm, SignInForm
from .mixins import IsLoggedInMixin, AccessToUpdate
from .models import User, Contact


# Create your views here.
class Login(IsLoggedInMixin, LoginView):
    form_class = SignInForm

    # redirect after login
    def get_success_url(self):
        return reverse('post:user_page', args=[self.request.user.username])


class Register(CreateView):
    # register a user
    model = User
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class EditProfile(UpdateView):
    # edit profile
    model = User
    fields = ["username", "biography", "profile"]

    # redirect after editing profile
    def get_success_url(self):
        return reverse("post:user_page", args=[self.request.user.username])


def follow_unfollow(request, username):
    # follow and unfollow a user
    user = get_object_or_404(User, username=username)
    try:
        Contact.objects.get(user_from=request.user, user_to=user).delete()
    except Contact.DoesNotExist:
        contact = Contact.objects.create(user_from=request.user, user_to=user)
        contact.save()
    return redirect("post:user_page", request.user.username)


def following_json(request, username):
    # will return a json that show are you following a person or no
    user = get_object_or_404(User, username=username)
    try:
        Contact.objects.get(user_from=request.user, user_to=user)
        following = True
    except Contact.DoesNotExist:
        following = False
    return JsonResponse({
        "following": following
    })
