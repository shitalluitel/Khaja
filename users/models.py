from datetime import datetime, timedelta

import jwt
import requests

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.conf import settings
from django.template.defaultfilters import safe
from django.utils.safestring import mark_safe
from company.models import Company
from .validators import UsernameValidator
from django.core.mail import EmailMessage
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have a valid email address.")

        if not kwargs.get('username'):
            raise ValueError('User must have a valid username')

        user = self.model(
            username=kwargs.get('username').strip(),
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name', None),
            last_name=kwargs.get('last_name', None),
            is_confirmed=kwargs.get('is_confirmed', False),
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """
    username = models.CharField(
        max_length=255,
        unique=True,
        validators=[UsernameValidator()],
        error_messages={
            'unique': 'User with this username already exists.',
        },
    )
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'User with this email already exists.',
        },
    )
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_type = models.IntegerField(default=0,validators=[MaxValueValidator(3), MinValueValidator(1)])
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    image = models.ImageField(upload_to="profile_picture/", default="profile_picture/none/no_image_user.png")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tag = True

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    #changed this part
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # @property
    # def is_admin(self):
    #     """
    #     Is the user a member of staff?
    #     """
    #     return self.is_staff

    def generate_confirmation_token(self):
        payload = {
            'confirm': self.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=7)
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return token

    def send_confirmation_email(self):
        token = self.generate_confirmation_token()
        link = settings.BASE_URL + 'users/confirm_email?token={}'.format(token)
        html = '<html><body>Click on the below link to confirm your email.<br> <a href="{}">{}</a></body></html>'.format(
            link, link)
        # data = {
        #     'from': "{} <{}>".format('Daily Cost', settings.ADMIN_EMAIL),
        #     'to': self.email,
        #     'subject': "Email Confirmation",
        #     'html': html | safe
        # }

        # requests.post(settings.MAILGUN_SERVER,
        #               auth=("api", settings.MAILGUN_API_KEY),
        #               data=data)
        print('http://localhost:8000/users/confirm_email?token={}'.format(token))

        print('http://khaja.herokuapp.com/users/confirm_email?token={}'.format(token))

        # for gmail mail confirmation api
        email = EmailMessage('subject: Email Confirmation ', html, to=[self.email])
        email.content_subtype = "html"
        # # email.attach(html)
        email.send()

    def generate_password_reset_token(self):
        payload = {
            'reset': self.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=7)
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return token

    def send_password_reset_email(self):
        token = self.generate_password_reset_token()
        link = settings.BASE_URL + 'users/password_reset?token={}'.format(token)
        # link = 'http://localhost' + '/users/password_reset?token={}'.format(token)
        html = '<html><body>Click on the below link to reset your password.<br> <a href="{}">{}</a></body></html>'.format(
            link, link)
        # data = {
        #     'from': "{} <{}>".format('Daily Cost', settings.ADMIN_EMAIL),
        #     'to': self.email,
        #     'subject': "Reset Password",
        #     'html': html
        # }

        # requests.post(settings.MAILGUN_SERVER,
        #               auth=("api", settings.MAILGUN_API_KEY),
        #               data=data)
        print('http://localhost:8000/users/password_reset?token={}'.format(token))

        print('http://khaja.herokuapp.com/users/password_reset?token={}'.format(token))
        # email = EmailMessage('subject: Reset Password ', html, to=[self.email])
        # email.content_subtype = "html"
        # # email.attach(html)
        # email.send()

    class Meta:
        db_table = "users"
