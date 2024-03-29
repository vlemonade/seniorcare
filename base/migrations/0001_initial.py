# Generated by Django 4.2.7 on 2024-01-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='osca_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('suffix', models.CharField(blank=True, max_length=5, null=True)),
                ('age', models.BigIntegerField(null=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('barangay', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('OSCA_ID', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='senior_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('suffix', models.CharField(blank=True, max_length=5, null=True)),
                ('age', models.BigIntegerField(null=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('barangay', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('OSCA_ID', models.CharField(max_length=20, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_claimed', models.BooleanField(default=False)),
                ('claimed_date', models.DateTimeField(blank=True, null=True)),
                ('senior_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('proof_of_claiming', models.ImageField(blank=True, null=True, upload_to='proof/')),
                ('status', models.BooleanField(default=True)),
                ('deletion_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_deletion', models.DateTimeField(blank=True, null=True)),
                ('allowance_type', models.CharField(blank=True, choices=[('none', 'Select Type of Allowance'), ('Monthly Monetary Allowance', 'Monthly Monetary Allowance')], max_length=50, null=True)),
                ('allowance_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMSMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_number', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
