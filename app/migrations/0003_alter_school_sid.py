# Generated by Django 4.2 on 2023-05-16 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_school_sname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Sid',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]
