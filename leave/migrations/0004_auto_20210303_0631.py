# Generated by Django 3.1.7 on 2021-03-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20210228_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
