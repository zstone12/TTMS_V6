# Generated by Django 2.2.1 on 2019-05-25 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_remove_ticket_sale_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='sale_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
