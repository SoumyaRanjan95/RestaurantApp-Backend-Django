# Generated by Django 5.1.3 on 2024-12-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0006_alter_orders_managers_alter_bills_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='slot',
            field=models.CharField(max_length=9),
        ),
    ]