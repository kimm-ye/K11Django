# Generated by Django 4.0 on 2022-01-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='my_file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
