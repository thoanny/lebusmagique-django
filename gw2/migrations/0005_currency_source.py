# Generated by Django 5.2.3 on 2025-07-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2', '0004_alter_item_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('icon', models.URLField(blank=True)),
                ('data', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField(blank=True)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
