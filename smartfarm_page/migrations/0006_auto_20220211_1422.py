# Generated by Django 3.2.9 on 2022-02-11 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm_page', '0005_delete_fileuploadmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InputValueModel',
        ),
        migrations.DeleteModel(
            name='PhoneNumberRegex',
        ),
    ]
