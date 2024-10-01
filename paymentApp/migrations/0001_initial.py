# Generated by Django 5.1 on 2024-09-25 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fare', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advance_payment_status', models.CharField(blank=True, choices=[('pending', 'pending'), ('paid', 'paid'), ('failed', 'failed')], max_length=30, null=True)),
                ('pending_payment_status', models.CharField(blank=True, choices=[('pending', 'pending'), ('paid', 'paid'), ('failed', 'failed')], max_length=30, null=True)),
                ('advance_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pending_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advance_payment_percent', models.CharField(blank=True, choices=[('25', '25'), ('50', '50')], max_length=10, null=True)),
                ('advance_payment_type', models.CharField(blank=True, choices=[('Wallet', 'Wallet'), ('credit', 'credit'), ('debit', 'debit')], max_length=20, null=True)),
                ('pending_paymeny_Type', models.CharField(blank=True, choices=[('upi', 'upi'), ('cash', 'cash'), ('wallet', 'wallet'), ('card', 'card'), ('netbanking', 'netbanking')], max_length=20, null=True)),
                ('advance_payment_date', models.DateTimeField(blank=True, null=True)),
                ('pending_payment_date', models.DateTimeField(blank=True, null=True)),
                ('advance_razorpay_payment_id', models.CharField(blank=True, null=True)),
                ('pending_razorpay_payment_id', models.CharField(blank=True, null=True)),
                ('ride', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customerApp.ride')),
            ],
        ),
    ]