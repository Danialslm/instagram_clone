# From Django
from django.db import models
from django.shortcuts import get_object_or_404

# From Apps
from User.models import User


# Managers
class PostManager(models.Manager):
    # like and dislike post
    def like_dislike(self, request, pk):
        post = get_object_or_404(self.model, pk=pk)
        if request.user not in post.like.all():
            post.like.add(request.user)
        else:
            post.like.remove(request.user)
        post.save()


# Models
class Post(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher')
    caption = models.TextField(null=True, blank=True)
    like = models.ManyToManyField(User, related_name="like", null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    content = models.ImageField(upload_to="images")
    objects = PostManager()

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.publisher.username

    def like_count(self):
        return self.like.count()

    like_count.short_description = "like count"
