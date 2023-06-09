# Generated by Django 2.2.12 on 2023-02-28 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penjadwalan', '0004_auto_20230228_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matakuliah',
            old_name='Dosen',
            new_name='dosen',
        ),
        migrations.RenameField(
            model_name='matakuliah',
            old_name='Matakuliah',
            new_name='matakuliah',
        ),
        migrations.RenameField(
            model_name='ruangan',
            old_name='Lab',
            new_name='lab',
        ),
        migrations.RemoveField(
            model_name='ruangan',
            name='matakuliah_id',
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='lab_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='penjadwalan.Ruangan'),
        ),
    ]
