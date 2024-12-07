# Generated by Django 5.1.3 on 2024-12-02 13:22

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0010_alter_orders_user_alter_reservations_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 2, 13, 22, 53, 186207, tzinfo=datetime.timezone.utc)),
        ),
    ]
