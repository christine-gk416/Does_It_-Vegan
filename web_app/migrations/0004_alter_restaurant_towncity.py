# Generated by Django 3.2 on 2022-03-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_auto_20220310_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='townCity',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
