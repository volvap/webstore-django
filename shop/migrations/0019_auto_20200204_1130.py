# Generated by Django 3.0.2 on 2020-02-04 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200204_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='items',
            new_name='item',
        ),
    ]
