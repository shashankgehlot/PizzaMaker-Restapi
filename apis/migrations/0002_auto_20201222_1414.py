# Generated by Django 3.1.4 on 2020-12-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza_size',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pizza_toppings',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pizza_type',
            name='id',
        ),
        migrations.AlterField(
            model_name='pizza_size',
            name='pizza_size',
            field=models.CharField(default='small', max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pizza_toppings',
            name='pizza_toppings',
            field=models.CharField(default='Olives', max_length=40, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='pizza_type',
            name='pizza_type',
            field=models.CharField(default='regular', max_length=40, primary_key=True, serialize=False),
        ),
    ]
