# Generated by Django 2.2.3 on 2019-07-27 14:22

from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_hash', models.CharField(default=orders.models._createIdOrder, max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('store', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.Store')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('meal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderMeal')),
            ],
        ),
    ]
