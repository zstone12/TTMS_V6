# Generated by Django 2.2.1 on 2019-05-25 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_ticket_sale_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sale_time',
        ),
    ]
