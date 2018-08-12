from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('event:list')), name='home'),
]