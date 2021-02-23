"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# From Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# From Apps
from User.views import Login

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('', include("django.contrib.auth.urls")),
    path('', include("Post.urls")),
    path('', include("User.urls")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:  # show media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
