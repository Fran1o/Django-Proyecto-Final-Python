# Generated by Django 4.1.4 on 2022-12-18 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comenapp', '0002_remove_coments_remitente'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='remitente',
            field=models.CharField(default=datetime.datetime(2022, 12, 18, 2, 37, 3, 645554, tzinfo=datetime.timezone.utc), max_length=30),
            preserve_default=False,
        ),
    ]