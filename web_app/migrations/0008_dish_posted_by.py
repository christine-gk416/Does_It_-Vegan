# Generated by Django 3.2 on 2022-04-23 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_app', '0007_alter_dish_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish_added', to=settings.AUTH_USER_MODEL),
        ),
    ]