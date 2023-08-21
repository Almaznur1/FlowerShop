# Generated by Django 4.2.4 on 2023-08-21 12:21

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_delete_activeorder_alter_order_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, db_index=True, default=django.utils.datetime_safe.datetime.now, verbose_name='Дата доставки'),
        ),
    ]
