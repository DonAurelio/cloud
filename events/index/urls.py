from django.urls import path

from index.views import Home

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
]