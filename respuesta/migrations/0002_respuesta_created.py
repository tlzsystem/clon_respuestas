# Generated by Django 3.0.2 on 2020-01-09 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('respuesta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]