# Generated by Django 5.2.3 on 2025-07-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2', '0007_alter_currency_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='data',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
