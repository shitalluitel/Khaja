from django.db import models
from products.models import Product
from users.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed, post_delete


# Create your models here.

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    products = models.ManyToManyField(Product, through='Quantity', blank=True)
    total = models.DecimalField(default=-0.00, max_digits=100, decimal_places=2)
    subtotal = models.DecimalField(default=-0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


class Quantity(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


def post_save_quantity_receiver(sender, instance, *args, **kwargs):
    calculate_total(instance)


post_save.connect(post_save_quantity_receiver, sender=Quantity)


def calculate_total(instance):
    try:
        products = Quantity.objects.all().filter(cart_id=instance.cart_id)
    except:
        products = instance
    cart = Cart.objects.get(id=instance.cart_id)
    total = 0
    for x in products:
        total += x.product.product_price * x.quantity
        print(x.product.product_price)
    print("Total: %s" % total)
    if cart.subtotal != total:
        cart.subtotal = total
        cart.save()


def post_delete_quantity_receiver(sender, instance, *args, **kwargs):
    calculate_total(instance=instance)


post_delete.connect(post_delete_quantity_receiver, sender=Quantity)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = float(instance.subtotal) * (1 + 0.1)
    else:
        instance.total = 0


pre_save.connect(pre_save_cart_receiver, sender=Cart)
