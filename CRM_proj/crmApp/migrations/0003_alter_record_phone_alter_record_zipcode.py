# Generated by Django 5.0.1 on 2024-02-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmApp', '0002_rename_reocord_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='zipcode',
            field=models.CharField(max_length=6),
        ),
    ]
