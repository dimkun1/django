"""
URL configuration for firstdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from firstdjango import settings
from myapp4.views import index, about
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),
    path('myapp1/', include('myapp1.urls')),
    path('myapp2/', include('myapp2.urls')),
    path('myapp4/', include('myapp4.urls')),
    path('myapp5/', include('myapp5.urls')),
    path('myapp6/', include('myapp6.urls')),
    path('myapp7/', include('myapp7.urls')),
    path('myapp9/', include('myapp9.urls')),
    path('', index),
    path('about/', about),
    # path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
