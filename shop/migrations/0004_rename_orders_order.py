# Generated by Django 4.0.1 on 2022-02-11 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders_alter_product_desc_alter_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
