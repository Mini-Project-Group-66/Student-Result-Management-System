# Generated by Django 4.2 on 2023-04-24 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declareresult',
            name='marks',
            field=models.JSONField(blank=True),
        ),
    ]
