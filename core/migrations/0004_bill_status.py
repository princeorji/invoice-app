# Generated by Django 4.0.1 on 2022-02-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_client_item_alter_bill_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'Pending'), (2, 'Paid')], default=1),
        ),
    ]