# Generated by Django 3.2.4 on 2021-07-01 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webRayoMakween', '0003_auto_20210701_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajos',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='trabajos',
            name='materiales',
        ),
    ]
