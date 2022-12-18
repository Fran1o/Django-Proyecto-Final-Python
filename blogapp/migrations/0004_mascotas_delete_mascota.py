# Generated by Django 4.1.3 on 2022-12-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_mascota_delete_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('animal', models.CharField(max_length=200)),
                ('raza', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Mascota',
        ),
    ]
