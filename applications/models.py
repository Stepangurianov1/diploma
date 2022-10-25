from django.db import models

from authapp.models import User
from mainapp.models import Product, Product_for_diller

colors_telephone = [
    ('black', 'black'),
    ('yellow', 'yellow'),
    ('white', 'white'),
]


class ApplicationModel(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    is_active = models.CharField(default='в обработке', max_length=128)

    def __str__(self):
        return f'{self.name}'


class MyProductsModel(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    name_application = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
    model = models.ForeignKey(Product_for_diller, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.model}'
