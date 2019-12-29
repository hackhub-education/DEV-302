from django.db import models


import datetime
from django.utils import timezone


class Prizes(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name+"("+str(self.amount)+")"

class User(models.Model):
    user_phone = models.IntegerField()
    prize_name = models.CharField(max_length=200)

    def __str__(self):
        return "user" + str(self.user_phone) + " win " + self.prize_name
