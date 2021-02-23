# From Django
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.html import format_html


# Managers
class ContactManager(models.Manager):
    # follow  a user
    def follow(self, request, user):
        contact = Contact.objects.create(user_from=request.user, user_to=user)
        contact.save()

    # unfollow a user
    def unfollow(self, request, user):
        return Contact.objects.get(user_from=request.user, user_to=user).delete()


# Models
class Contact(models.Model):
    # user_from is who you following
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rel_from_set")
    # user_to is who following you
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rel_to_set")

    def save(self, *args, **kwargs):
        # check the following is valid
        if self.user_from == self.user_to:
            raise ValidationError("can not follow yourself")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"


class User(AbstractUser):
    following = models.ManyToManyField("self", through=Contact, related_name="followers")
    profile = models.ImageField(upload_to="profiles", default="profiles/default-profile-user.jpg")
    biography = models.TextField(blank=True, null=True)

    # redirect after register a user
    def get_absolute_url(self):
        return reverse("login")

    # get following count
    def following_count(self):
        return self.following.count()

    # get followers count
    def followers_count(self):
        return Contact.objects.filter(user_to=self).count()

    # show user's profile in admin panel
    def show_profile(self):
        return format_html(f"<img src='{self.profile.url}' alt={self.username}' width='60px'>")

    following_count.short_description = "following"
    followers_count.short_description = "followers"
    show_profile.short_description = "profile"
