# Generated by Django 2.2.19 on 2021-02-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]