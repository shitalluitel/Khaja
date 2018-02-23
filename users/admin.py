from django.contrib import admin

# Register your models here.

fields = ['image_tag']
readonly_fields = ['image_tag']

from .models import User

admin.site.register(User)
