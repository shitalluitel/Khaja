from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinLengthValidator
from company.models import Company

# Create your models here.

class Product(models.Model):
    company = models.ForeignKey(Company, related_name='product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    time = models.IntegerField(default=5, validators=[MaxValueValidator(200)])
    image = models.ImageField(upload_to="dishes/", default=None, null=False, blank=True)
    description = models.TextField(max_length=512, validators=[MinLengthValidator(120)])

    # featured = models.BooleanField(default=False)
    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tag = True
