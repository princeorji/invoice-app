from django.db import models
from django.db.models import F, Sum
from django.contrib.auth.models import User

from decimal import Decimal
from shortuuidfield import ShortUUIDField

# Create your models here.

class Invoice(models.Model):
    PAYMENT_STATUS = (
        (1, 'Pending'),
        (2, 'Paid')
    )
    uuid = ShortUUIDField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    created_on =  models.DateField(auto_now_add=True)
    status = models.PositiveIntegerField(choices=PAYMENT_STATUS, default='pending')

    def __str__(self):
        return self.name

class Service(models.Model):
    service = models.CharField(max_length=25)
    quantity = models.IntegerField(default=1)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    due_date = models.DateField()

    @property
    def rate_display(self):
        return "$%s" % self.rate

    @property
    def total_price(self):
        return self.service_set.aggregate(
            total_price=Sum(F('quantity') * F('rate'))
        )['total_price'] or Decimal('0')

    def __str__(self):
        return self.service

