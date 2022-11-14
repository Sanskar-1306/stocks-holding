# Generated by Django 4.1.3 on 2022-11-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('trade_type', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cummulative_allocation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bal_quantity', models.IntegerField()),
                ('avg_purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
