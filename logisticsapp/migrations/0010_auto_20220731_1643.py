# Generated by Django 3.2.12 on 2022-07-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsapp', '0009_auto_20220731_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='adhar_card_back_side_img',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='adhar_card_back_side_img_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='adhar_card_front_side_img',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='adhar_card_front_side_img_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='permit_front_side_img',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='permit_front_side_img_path',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pollution_certificate_front_side_img',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pollution_certificate_front_side_img_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration_certificate_back_side_img',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration_certificate_back_side_img_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration_certificate_front_side_img',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration_certificate_front_side_img_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
