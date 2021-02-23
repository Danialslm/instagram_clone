# From Django
from django.http import Http404
from django.shortcuts import get_object_or_404

# From Apps
from .models import Post


class AccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        # check post's publisher is who wanna update it.
        post = get_object_or_404(Post, pk=pk)
        if post.publisher == request.user:
            return super().dispatch(request, *args, **kwargs)
        raise Http404()
