# Generated by Django 5.0.2 on 2024-12-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventregistration_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='screenshot',
            field=models.ImageField(default='screenshots/default.png', upload_to='screenshots/'),
        ),
    ]
