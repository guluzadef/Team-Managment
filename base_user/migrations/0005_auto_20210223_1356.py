# Generated by Django 2.2.19 on 2021-02-23 13:56

import base_user.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0004_auto_20210223_1311'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', base_user.models.MyUserManager()),
            ],
        ),
    ]
