# Generated by Django 3.2.9 on 2022-02-11 00:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='InputValueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chojang', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumberRegex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex='?([0-9]{3,4})-?([0-9]{4})$')])),
            ],
        ),
    ]
