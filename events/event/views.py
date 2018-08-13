from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from event.models import Event


class EventList(LoginRequiredMixin,ListView):
    """Deals with events list logic."""

    model = Event
    template_name = 'event/event_list.html'

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'

    # def get_queryset(self):
    #     queryset = Event.objects.filter(user=self.request.user)
    #     return queryset


class EventDetail(LoginRequiredMixin,DetailView):
    """Deals with event creation logic."""

    model = Event
    template_name = 'event/event_detail.html'

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'


class EventUpdate(LoginRequiredMixin,UpdateView):
    """Deals with event update logic."""

    model = Event
    fields = [
        'name','venue','address','start_date','end_date',
        'category','classification'
    ]

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'


class EventDelete(LoginRequiredMixin,DeleteView):
    """Deals with event delection logic."""
    model = Event
    success_url = reverse_lazy('event:list')

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'


class EventCreate(LoginRequiredMixin,CreateView):
    """Deals with event creation logic."""

    model = Event
    fields = [
        'name','venue','address','start_date','end_date',
        'category','classification'
    ]
    success_url = reverse_lazy('event:list')

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    