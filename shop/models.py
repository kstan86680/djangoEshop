from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(default='/media/404.png', upload_to='shop/', height_field=None, width_field=None, max_length=None)
    featured = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

