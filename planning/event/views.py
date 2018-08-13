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

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:

            """
            Filtering events by user. i.e., each user
            will see their own events.
            """
            queryset = self.model._default_manager.filter(user=self.request.user)
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


class EventDetail(LoginRequiredMixin,DetailView):
    """Deals with event creation logic."""

    model = Event
    template_name = 'event/event_detail.html'

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        """
        Return the `QuerySet` that will be used to look up the object.
        This method is called by the default implementation of get_object() and
        may not be called if get_object() is overridden.
        """
        if self.queryset is None:
            if self.model:
                """
                Filtering events by user. i.e., each user
                will see their own events.
                """
                return self.model._default_manager.filter(user=self.request.user)
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()


class EventUpdate(LoginRequiredMixin,UpdateView):
    """Deals with event update logic."""

    model = Event
    fields = [
        'name','venue','address','start_date','end_date',
        'category','classification'
    ]

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'


    def get_queryset(self):
        """
        Return the `QuerySet` that will be used to look up the object.
        This method is called by the default implementation of get_object() and
        may not be called if get_object() is overridden.
        """
        if self.queryset is None:
            if self.model:
                """
                Filtering events by user. i.e., each user
                will see their own events.
                """
                return self.model._default_manager.filter(user=self.request.user)
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()


class EventDelete(LoginRequiredMixin,DeleteView):
    """Deals with event delection logic."""
    model = Event
    success_url = reverse_lazy('event:list')

    login_url = 'authentication:login'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        """
        Return the `QuerySet` that will be used to look up the object.
        This method is called by the default implementation of get_object() and
        may not be called if get_object() is overridden.
        """
        if self.queryset is None:
            if self.model:
                """
                Filtering events by user. i.e., each user
                will see their own events.
                """
                return self.model._default_manager.filter(user=self.request.user)
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()


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
    