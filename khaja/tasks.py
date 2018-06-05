from celery.decorators import task
from datetime import timedelta
import time
from carts.models import Cart
from django.utils import timezone

@task()
def display():
    date_from = timezone.now()
    while True:
        date_from = timezone.now() - timedelta(minutes=10)
        Cart.objects.filter(is_active=True, created_at__lte=date_from).delete()
        time.sleep(10)


# def
