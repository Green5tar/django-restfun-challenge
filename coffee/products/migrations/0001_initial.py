# Generated by Django 4.0.2 on 2022-02-01 21:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.utcnow)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.utcnow)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, choices=[('Latte', 'Latte'), ('Cappuccino', 'Cappuccino'), ('Espresso', 'Espresso'), ('Tea', 'Tea'), ('Hot chocolate', 'Hot chocolate'), ('Cookie', 'Cookie')], max_length=512, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=10.0, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AvailableProductOption',
            fields=[
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.utcnow)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.utcnow)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, choices=[('Latte', 'Latte'), ('Cappuccino', 'Cappuccino'), ('Espresso', 'Espresso'), ('Tea', 'Tea'), ('Hot chocolate', 'Hot chocolate'), ('Cookie', 'Cookie')], max_length=512, null=True)),
                ('option', models.CharField(blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Single', 'Single'), ('Double', 'Double'), ('Triple', 'Triple'), ('Chocolate', 'Chocolate'), ('Chip', 'Chip'), ('Ginger', 'Ginger'), ('take away', 'take away'), ('In shop', 'In shop')], max_length=512, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
