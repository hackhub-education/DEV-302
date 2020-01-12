from django.db import models

STATUS_LIST = [
    ("new", 1),
    ("used", 0)
]


class Coupon(models.Model):
    name = models.CharField(max_length=300)
    # coupon_code = models.CharField(max_length=8) #todo:
    # todo: we do not generate coupon code for now, use id as coupon code for now
    # todo: QR code in the future
    discount = models.IntegerField()
    value = models.FloatField()
    modified_by = models.CharField(max_length=100)
    send_to = models.CharField(max_length=100)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(choices=STATUS_LIST, default='new', max_length=50)

    def __str__(self):
        return self.name + " (Discount: " + str(self.discount) + "%)"
