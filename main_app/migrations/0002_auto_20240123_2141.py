# Generated by Django 3.2.12 on 2024-01-23 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('drink_id', models.CharField(max_length=20)),
                ('drink_image', models.CharField(max_length=255)),
                ('ingredient_1', models.CharField(max_length=255)),
                ('ingredient_2', models.CharField(max_length=255)),
                ('ingredient_3', models.CharField(max_length=255)),
                ('ingredient_4', models.CharField(max_length=255)),
                ('ingredient_5', models.CharField(max_length=255)),
                ('ingredient_6', models.CharField(max_length=255)),
                ('ingredient_7', models.CharField(max_length=255)),
                ('ingredient_8', models.CharField(max_length=255)),
                ('ingredient_9', models.CharField(max_length=255)),
                ('ingredient_10', models.CharField(max_length=255)),
                ('ingredient_11', models.CharField(max_length=255)),
                ('ingredient_12', models.CharField(max_length=255)),
                ('ingredient_13', models.CharField(max_length=255)),
                ('ingredient_14', models.CharField(max_length=255)),
                ('ingredient_15', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]