from django.db import models


import datetime
from django.utils import timezone


class Prizes(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name+str(self.amount)



class Users(models.Model):
    Phone = models.CharField(max_length=200)
    price = models.ForeignKey(Prizes, on_delete=models.CASCADE)

    def __str__(self):
        return self.Phone+str(self.price)
