from django.db import models
from users.models import User
from carts.models import Cart

# Create your models here.
STATES = (
    ('01','Province No. 1'),
    ('02','Province No. 2'),
    ('03','Province No. 3'),
    ('04','Gandaki Pradesh'),
    ('05','Province No. 5'),
    ('06','Karnali Pradesh'),
    ('07','Province No. 6'),
)

class Address(models.Model):
    # user = models.ForeignKey(User)
    # address_type = models.CharField(max_length=120)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, default='Biratnagar', null=True, blank=True)
    country = models.CharField(max_length=120, default='Nepal', null=True, blank=True)
    cart = models.ForeignKey(Cart, blank=True, null=True)
    state = models.CharField(max_length=120, choices= STATES, default='01', null=True, blank=True)
    phone_number = models.CharField(max_length=16)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.address_line_1)

    class Meta:
        db_table = "addresses"
