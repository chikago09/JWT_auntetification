from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=1000000)
    description = models.CharField(max_length=10000)
    release_date = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.name

