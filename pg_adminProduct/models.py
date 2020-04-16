from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50)
    price = models.CharField(
        max_length=50)
    priceSale = models.CharField(
        max_length=50)
    size = models.CharField(
        max_length=50)
    productImg = models.ImageField(

        upload_to='images/'
    )


def __str__(self):
    return '{}'.format(self.name, self.price, self.priceSale, self.size)


def save(self, **kwargs):
    super(Product, self).save()


class Meta:
    verbose_name_plural = "Products"
