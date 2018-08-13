# -*- encoding: utf-8 -*-

from django.urls import path
from authentication.views import *
from authentication.forms import *

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
]
