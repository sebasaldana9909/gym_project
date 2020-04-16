from django.db import models


class Client(models.Model):
    name = models.CharField(
        max_length=50)
    email = models.CharField(
        max_length=50)
    telefono = models.CharField(
        max_length=50)
    monto = models.CharField(
        max_length=50)


def __str__(self):
    return '{}'.format(self.name, self.email, self.telefono, self.monto)


def save(self, **kwargs):
    super(Client, self).save()


class Meta:
    verbose_name_plural = "Clients"


from django.db import models

# Create your models here.
