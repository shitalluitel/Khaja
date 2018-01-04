from django.db import models
from django.utils.safestring import mark_safe

from users.models import User


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    product_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="dishes/", default=None, null=False, blank=True)
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tag = True
