# Generated by Django 4.2.10 on 2024-10-20 03:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Votacion', '0003_alter_voto_tipo_voto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='fecha_voto',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]