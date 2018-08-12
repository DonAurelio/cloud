from django.urls import path

from event.views import EventList

urlpatterns = [
    path('', EventList.as_view(), name='list'),
]