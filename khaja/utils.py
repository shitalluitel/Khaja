import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
    order_new_id = random_string_generator()

    klass = instance.__class__
    qs_exist = klass.objects.filter(order_id=order_new_id).exists()
    if qs_exist:
        return unique_order_id_generator()
    return order_new_id


def unique_company_id_generator(instance):
    company_new_id = random_string_generator()

    klass = instance.__class__
    qs_exist = klass.objects.filter(company_id=company_new_id).exists()
    if qs_exist:
        return unique_company_id_generator()
    return company_new_id


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
