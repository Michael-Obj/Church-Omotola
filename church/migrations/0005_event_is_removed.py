# Generated by Django 5.0.2 on 2024-03-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0004_team_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_removed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]