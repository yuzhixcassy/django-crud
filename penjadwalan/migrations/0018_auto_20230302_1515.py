# Generated by Django 2.2.12 on 2023-03-02 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjadwalan', '0017_auto_20230302_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruangan',
            name='lab',
            field=models.CharField(max_length=50),
        ),
    ]
