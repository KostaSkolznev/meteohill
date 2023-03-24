from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]