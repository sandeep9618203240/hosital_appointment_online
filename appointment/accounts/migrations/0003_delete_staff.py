# Generated by Django 5.0.4 on 2024-06-03 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_patient_staff'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
