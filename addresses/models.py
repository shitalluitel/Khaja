from django.db import models
from users.models import User


# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User)
    # address_type = models.CharField(max_length=120)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='Nepal')
    state = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=16)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.address_line_1)
