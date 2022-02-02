from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    organisation = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Bill(models.Model):
    item = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    hours = models.IntegerField(default=1)
    pay_date = models.DateField()

    @property
    def rate_display(self):
        return "$%s" % self.rate

    def __str__(self):
        return self.item
