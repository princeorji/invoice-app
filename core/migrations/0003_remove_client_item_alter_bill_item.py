# Generated by Django 4.0.1 on 2022-02-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_bill_pay_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='item',
        ),
        migrations.AlterField(
            model_name='bill',
            name='item',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
