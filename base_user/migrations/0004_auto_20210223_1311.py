# Generated by Django 2.2.19 on 2021-02-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0003_auto_20210223_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
    ]
