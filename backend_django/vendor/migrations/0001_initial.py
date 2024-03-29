# Generated by Django 2.2.3 on 2019-07-27 11:57

from django.db import migrations, models
import django.db.models.deletion
import vendor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_hash', models.CharField(default=vendor.models._createIdMeal, max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_hash', models.CharField(default=vendor.models._createIdQuestion, max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
                ('option_limit_lower', models.IntegerField(null=True)),
                ('option_limit_upper', models.IntegerField(null=True)),
                ('meal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_hash', models.CharField(default=vendor.models._createIdOption, max_length=32, primary_key=True, serialize=False)),
                ('option_text', models.CharField(max_length=255)),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.Question')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.Store'),
        ),
    ]
