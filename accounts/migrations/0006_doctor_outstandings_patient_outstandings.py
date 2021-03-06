# Generated by Django 3.0.5 on 2020-05-25 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_appointments_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Outstandings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outstanding', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Outstandings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outstanding', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Patient')),
            ],
        ),
    ]
