from django.db import models
from django.db.models import F, Sum
from django.core.validators import RegexValidator
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
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_on =  models.DateField(auto_now_add=True)
    status = models.PositiveIntegerField(choices=PAYMENT_STATUS)

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

