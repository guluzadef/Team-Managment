# Generated by Django 2.2.19 on 2021-02-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='about'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='coverphoto'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='location',
            field=models.CharField(blank=True, max_length=150, verbose_name=' location'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='', verbose_name='profilephoto'),
        ),
    ]
