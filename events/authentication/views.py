# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.views.generic import TemplateView
# from django.contrib.auth import authenticate, login
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib import auth 
# from django.contrib import messages
# from django.views.generic.list import ListView
# from .models import Account


# class Login(TemplateView):

#     def get(self,request,*args,**kwargs):
#         return render_to_response(
#             'authentication/login.html',
#             context_instance=RequestContext(request)
#             )

#     def post(self,request,*args,**kwargs):
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('start:index'))
#             else:
#                 messages.error(request,'La contraseña es invalida, o el usuario esta inactivo')
#         else:
#             # the authentication system was unable to verify the username and password
#             messages.error(request,'El usuario o la contraseña son incorrectos')

#         return render_to_response('authentication/login.html',context_instance = RequestContext(request))


# class Logout(TemplateView):
#     def get(self,request,*args,**kwargs): 
#         auth.logout(request)    
#         return render_to_response(
#             'authentication/login.html',
#             context_instance=RequestContext(request)
#             )

from django.contrib.auth import views


class Login(views.LoginView):
    """Deals with user authentication and login processes."""

    # The name of a template to display for the view used to log the user in.
    template_name = 'authentication/login.html'
    # A boolean that controls whether or not authenticated users accessing the 
    # login page will be redirected as if they had just successfully logged in. 
    redirect_authenticated_user = True
    # The redirec URL is defined in settings LOGIN_REDIRECT_URL


class Logout(views.LogoutView):
    """Deals with user logout process."""

    # The URL to redirect to after logout. Defaults to settings.LOGOUT_REDIRECT_URL.
    next_page = '/'