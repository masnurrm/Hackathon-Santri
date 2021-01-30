# Generated by Django 3.1 on 2021-01-20 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20210120_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayatpenyakit',
            name='dilaporkan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='nomor_induk'),
        ),
    ]
