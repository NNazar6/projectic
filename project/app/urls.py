from django.urls import path
from.views import index, registr

urlpatterns = [
    path('', index, name='Registration windows'),
    path('login', registr, name='input')
]