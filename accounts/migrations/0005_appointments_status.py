# Generated by Django 3.0.5 on 2020-05-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_appointments_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], default=1, max_length=100, null=True),
        ),
    ]
