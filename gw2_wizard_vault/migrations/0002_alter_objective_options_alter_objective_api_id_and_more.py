# Generated by Django 5.2.3 on 2025-07-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2_wizard_vault', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objective',
            options={'verbose_name': 'Objectif', 'verbose_name_plural': 'Objectifs'},
        ),
        migrations.AlterField(
            model_name='objective',
            name='api_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID API'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='tip',
            field=models.TextField(blank=True, verbose_name='Conseil'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Titre'),
        ),
    ]
