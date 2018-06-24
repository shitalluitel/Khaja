from django.db import models
from khaja.utils import unique_company_id_generator
from django.db.models.signals import pre_save

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=120)
    company_id = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


def pre_save_create_company_id(sender, instance, *args, **kwargs):
    if not instance.company_id:
        instance.company_id = unique_company_id_generator(instance)

pre_save.connect(pre_save_create_company_id, sender=Company)
