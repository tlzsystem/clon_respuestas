# Generated by Django 3.0.2 on 2020-01-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='comentario',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
