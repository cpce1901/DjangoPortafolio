# Generated by Django 5.0.3 on 2024-03-25 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0002_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='sensor',
            new_name='place',
        ),
    ]