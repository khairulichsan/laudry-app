# Generated by Django 5.1.2 on 2024-12-03 02:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuci', '0002_cuciorder_debt'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nomor_hp', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cuciorder',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='cuciorder',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuci.inputcustomer'),
        ),
    ]
