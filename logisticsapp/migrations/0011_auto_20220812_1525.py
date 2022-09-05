# Generated by Django 3.2.12 on 2022-08-12 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsapp', '0010_auto_20220731_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logisticsapp.customuser'),
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logisticsapp.customuser'),
        ),
    ]