from django.http import Http404
from django.shortcuts import get_object_or_404

from User.models import User


class IsLoggedInMixin:
    def dispatch(self, request):
        if request.user.is_anonymous:
            return super().dispatch(request)
        raise Http404()


class AccessToUpdate:
    def dispatch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user == user:
            print(request.user.username)
            return super().dispatch(request, pk)
        raise Http404()
