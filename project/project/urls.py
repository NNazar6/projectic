
from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('valid', include('app.urls')),
    path('login', include('app.urls')),
]
