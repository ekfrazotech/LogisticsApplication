# Generated by Django 3.2.12 on 2022-07-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsapp', '0007_auto_20220731_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='fitness_certificate_front_side_img',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='fitness_certificate_front_side_img_path',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
