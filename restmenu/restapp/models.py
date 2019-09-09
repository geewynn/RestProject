from django.db import models


# Create your models here.


class Restaurants(models.Model):
    restaurant_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    restaurant_name = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name='restaurants', null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(max_length=250)
    price = models.CharField(max_length=8)
    course = models.CharField(max_length=250)