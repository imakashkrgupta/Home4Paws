# Generated by Django 5.0.4 on 2024-11-21 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_pet_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pet_data',
        ),
    ]
