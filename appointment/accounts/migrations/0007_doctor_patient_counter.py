# Generated by Django 5.0.4 on 2024-06-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='patient_counter',
            field=models.IntegerField(default=0),
        ),
    ]
