# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_emision', models.DateField()),
                ('precio', models.DecimalField(max_digits=8, decimal_places=2)),
                ('adquiriente', models.CharField(max_length=10)),
                ('puesto', models.IntegerField()),
            ],
        ),
    ]
