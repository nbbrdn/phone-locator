# Generated by Django 5.0.1 on 2024-02-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0002_remove_defcode_locator_def_start_r_f6c9cd_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defcode',
            name='region',
            field=models.CharField(max_length=500),
        ),
    ]