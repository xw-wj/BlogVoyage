# Generated by Django 5.0.1 on 2024-11-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captchamodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
