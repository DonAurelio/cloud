# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.core import validators


# Extracted from https://thinkster.io/django-angularjs-tutorial
class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_superuser, is_active,**extra_fields):
        """
        Creates and save a User with the given username, email and password.
        """    
        if not email:
            raise ValueError('El campo email es necesario')

        account = self.model(
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_active=is_active
        )

        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_user(self, email, password=None,**extra_fields):
        return self._create_user(username,email,password,False,True,**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email,password,True,True,**extra_fields)


# Extracted from https://thinkster.io/django-angularjs-tutorial
# User model doc https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.models.User
# Example https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
class Account(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(_('email address'),unique=True, blank=True)
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    # To use the email as a username for login porpuses
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def is_admin(self):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        
        return self.email

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)