# Generated by Django 3.2.12 on 2022-07-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsapp', '0003_auto_20220504_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='whatsup_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]