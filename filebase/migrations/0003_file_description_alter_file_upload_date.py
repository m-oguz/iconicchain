# Generated by Django 4.2.6 on 2023-12-15 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filebase', '0002_file_company_file_upload_date_file_uploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.TextField(default='Description of the file', max_length=400),
        ),
        migrations.AlterField(
            model_name='file',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 3, 4, 56, 181928)),
        ),
    ]