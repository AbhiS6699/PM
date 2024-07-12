# Generated by Django 5.0.4 on 2024-05-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_listing_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
