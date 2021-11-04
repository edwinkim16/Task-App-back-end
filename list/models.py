from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_size =models.IntegerField()
    product_price = models.IntegerField()

    def __str__(self):
        self.name = self.product_name