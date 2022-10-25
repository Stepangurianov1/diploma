from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_image', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name}'


class Product_for_diller(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=128, blank=True)
    model = models.CharField(max_length=128)
    memory_size = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.model}'
