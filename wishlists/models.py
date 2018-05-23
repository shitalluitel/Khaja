from django.db import models
from users.models import User
from products.models import Product


# Create your models here.

class WishList(models.Model):
    user = models.ForeignKey(User, related_name="wishlist", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)
