from django.db import models
from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    basic_info = models.CharField(max_length=1000, default='Basic Information')
    upload = models.ImageField(upload_to="gallery/")
    slug = models.SlugField()

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
