from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from event.models import Event


class EventList(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'event/event_list.html'

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'
    