# Generated by Django 5.1.1 on 2024-10-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_on_vacation',
            field=models.BooleanField(default=False),
        ),
    ]
