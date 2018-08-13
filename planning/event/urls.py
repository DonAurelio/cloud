from django.urls import path

from event.views import EventList
from event.views import EventDetail
from event.views import EventUpdate
from event.views import EventDelete
from event.views import EventCreate

urlpatterns = [
    path('list/', EventList.as_view(), name='list'),
    path('add/', EventCreate.as_view(), name='add'),
    path('detail/<int:pk>/', EventDetail.as_view(), name='detail'),
    path('update/<int:pk>/', EventUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', EventDelete.as_view(), name='delete'),
]