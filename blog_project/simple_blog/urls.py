from django.contrib import admin
from django.urls import path, include
from .view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('', home),
]