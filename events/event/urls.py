from django.urls import path

from event.views import EventList
from event.views import EventDetail

urlpatterns = [
    path('list/', EventList.as_view(), name='list'),
    path('<slug:slug>/', EventDetail.as_view(), name='detail'),
]