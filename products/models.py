
import os
from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinLengthValidator
from company.models import Company
from django.utils.encoding import smart_text
from django.dispatch import receiver
# Create your models here.
class ProductModelQuerySet(models.query.QuerySet):
    # this method is used to delete item in two different fashion

    def deleteItem(self, *args, **kwargs):
        datas = self.filter(*args, **kwargs)
        data = datas.first()
        is_active = data.is_active

        print(is_active)
        #soft delete part
        if is_active:
            datas.update(is_active=False)
            print("Soft Delete")

        #hard delete part
        else:
            datas.delete()

            print("Deleted")
        print(type(data))
        return data

    def  restore(self, *args, **kwargs):
        product = self.filter(*args, **kwargs)
        product.update(is_active=True)
        return product

    def inactive(self,*args, **kwargs):
        return super(ProductModelQuerySet, self).filter(*args, **kwargs, is_active=False)



class ProductModelManager(models.Manager):
    # def get_queryset(self):
    #     return ProductModelQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return super(ProductModelManager, self).all(*args, **kwargs).filter(is_active=True)



class Product(models.Model):
    company = models.ForeignKey(Company, related_name='product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    time = models.IntegerField(default=5, validators=[MaxValueValidator(200)])
    image = models.ImageField(upload_to="dishes/", default=None, null=False, blank=True)
    description = models.TextField(max_length=512, validators=[MinLengthValidator(120)])
    is_active = models.BooleanField(default=True)
    # featured = models.BooleanField(default=False)

    objects = ProductModelManager.from_queryset(ProductModelQuerySet)()
    # yeso garda khera 2 tai le custome query set jastai kam garxa

    def __str__(self):
        return smart_text(self.product_name)

    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tag = True


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """
    Deletes image from imagesystem
    when corresponding `Mediaimage` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Product)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Deletes old image from imagesystem
    when corresponding `Mediaimage` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_image = Product.objects.get(pk=instance.pk).image
    except Product.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
