# Generated by Django 3.0.2 on 2020-01-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='upload',
            field=models.ImageField(default='img', upload_to='uploads/'),
        ),
    ]
