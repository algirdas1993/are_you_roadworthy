# Generated by Django 3.2.14 on 2022-07-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('car_reg_number', models.CharField(max_length=6, null=True)),
                ('check_date', models.DateField(null=True)),
                ('check_time', models.TimeField()),
            ],
        ),
    ]
