from django.db import models
from products.models import Product
from users.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed, post_delete


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id, is_active=True)
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
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


class Quantity(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(id)

    def calculate_total(self):
        try:
            products = Quantity.objects.all().filter(cart_id=self.cart_id)
        except:
            products = self
        print(self.cart_id)
        if self.cart_id:
            try:
                cart = Cart.objects.get(id=self.cart_id)
            except:
                return
            total = 0
            for x in products:
                total += x.product.product_price * x.quantity
            if cart.subtotal != total:
                cart.subtotal = total
                cart.save()


def post_save_quantity_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.calculate_total()


post_save.connect(post_save_quantity_receiver, sender=Quantity)


def post_delete_quantity_receiver(sender, instance, *args, **kwargs):
    instance.calculate_total()


post_delete.connect(post_delete_quantity_receiver, sender=Quantity)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = float(instance.subtotal) * (1 + 0.1)
    else:
        instance.total = 0


pre_save.connect(pre_save_cart_receiver, sender=Cart)
