# Generated by Django 2.1.2 on 2019-10-09 03:09

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0025_auto_20191008_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.CharField(choices=[('RUNNING', 'running'), ('CREATING', 'creating'), ('UNKNOWN', 'unknown')], default='UNKNOWN', max_length=128),
        ),
        migrations.AlterField(
            model_name='package',
            name='meta',
            field=common.models.JsonDictTextField(default={}),
        ),
    ]
