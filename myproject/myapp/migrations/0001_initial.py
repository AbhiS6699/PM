# Generated by Django 5.0.4 on 2024-05-13 19:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colony_name', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price_range', models.CharField(max_length=255)),
                ('builder_name', models.CharField(max_length=255)),
                ('property_type', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='properties/')),
                ('project_size', models.CharField(blank=True, max_length=100)),
                ('possession_date', models.DateField(blank=True, null=True)),
                ('total_units', models.IntegerField(blank=True, null=True)),
                ('total_towers', models.IntegerField(blank=True, null=True)),
                ('project_type', models.CharField(blank=True, max_length=255)),
                ('plot_size', models.CharField(blank=True, max_length=255)),
                ('project_status', models.CharField(blank=True, max_length=255)),
                ('rera_registraion', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PressImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='press_images/')),
                ('press', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.press')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='HomeLoanOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bank_img', models.ImageField(blank=True, upload_to='bank_img/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_offers', to='myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255)),
                ('rating', models.PositiveSmallIntegerField()),
                ('comment', models.TextField()),
                ('review_date', models.DateField(default=django.utils.timezone.now)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_reviews', to='myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(blank=True, upload_to='amenity_icons/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.property')),
            ],
        ),
    ]