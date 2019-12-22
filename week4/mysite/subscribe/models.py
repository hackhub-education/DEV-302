from django.db import models


import datetime
from django.utils import timezone


class Subscriber(models.Model):
    email = models.CharField(max_length=200)
    # status = 1: active   = 2 inactive
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.email + "(Status: " + str(self.status) + ")"
