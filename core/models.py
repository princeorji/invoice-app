from django.db import models
from shortuuidfield import ShortUUIDField
from django.core.validators import RegexValidator

# Create your models here.

class Invoice(models.Model):
    uuid = ShortUUIDField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    organisation = models.CharField(max_length=50, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Service(models.Model):
    PAYMENT_STATUS = (
        (1, 'Pending'),
        (2, 'Paid')
    )
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    due_date = models.DateField()
    status = models.PositiveIntegerField(choices=PAYMENT_STATUS, default=1)

    @property
    def rate_display(self):
        return "$%s" % self.rate

    def __str__(self):
        return f"{self.service}"
