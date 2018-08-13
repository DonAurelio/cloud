from django import forms
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect

from authentication.models import Account


# Reference: Django 1.8 Github
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class Register(TemplateView):
    """
    Deals with user registration. 
    """

    def get(self,request,*args,**kwargs):
        """
        Return a form for user registartion.
        """
        form = UserCreationForm()
        context = {'form':form}
        template = 'authentication/register.html'
        return render(request,template,context)

    def post(self,request,*args,**kwargs):
        """
        Proccesses user registration form.
        """
        form = UserCreationForm(request.POST)
        context = {}
        template = ''

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponseRedirect(reverse('index:home'))

        else:
            context['form'] = form
            template = 'authentication/register.html'

        return render(request,template, context)
