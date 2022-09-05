# Generated by Django 3.2.12 on 2022-04-04 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_plan_name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('validity_period', models.CharField(blank=True, max_length=250, null=True)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp')),
                ('last_update_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_update_timestamp')),
            ],
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='owner',
            new_name='driving_license_image_path',
        ),
        migrations.RenameField(
            model_name='dropdetails',
            old_name='drop_date_time',
            new_name='drop_date',
        ),
        migrations.RenameField(
            model_name='pickupdetails',
            old_name='pickup_date_time',
            new_name='pickup_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password',
        ),
        migrations.AddField(
            model_name='customuser',
            name='base64',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image_path',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='base64',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='license_status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='owner_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='validity_end_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='validity_start_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='dropdetails',
            name='drop_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='pickupdetails',
            name='pickup_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='placedorder',
            name='vehicle_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logisticsapp.vehicletypes'),
        ),
        migrations.AddField(
            model_name='status',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp'),
        ),
        migrations.AddField(
            model_name='status',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_update_timestamp'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_update_timestamp'),
        ),
        migrations.AddField(
            model_name='vehicletypes',
            name='per_km_price',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='placedorder',
            name='drop',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='create_timestamp'),
        ),
        migrations.AlterField(
            model_name='review',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_update_timestamp'),
        ),
        migrations.AddField(
            model_name='driver',
            name='subcription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logisticsapp.subscription'),
        ),
    ]