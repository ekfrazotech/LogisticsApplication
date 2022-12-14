# Generated by Django 3.2.12 on 2022-05-04 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logisticsapp', '0002_auto_20220404_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='validity_end_date',
            new_name='validity_end_date_time',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='validity_start_date',
            new_name='validity_start_date_time',
        ),
        migrations.AddField(
            model_name='customuser',
            name='pan_card',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pan_card_base64',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pan_image_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='driver_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='emission_test_expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='emission_test_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='fitness_certificate_expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='fitness_certificate_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='insurence_expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='insurence_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='license_expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='license_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='passbook_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='permit_expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='permit_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rc_expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rc_img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehicletypes',
            name='badge',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehicletypes',
            name='max_time_min',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehicletypes',
            name='min_charge',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicletypes',
            name='per_km_price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_holder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('account_no', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=100, null=True)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('last_update_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_update_timestamp')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logisticsapp.account'),
        ),
    ]
