# Generated by Django 3.2.14 on 2022-07-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_bookingtime_check_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtime',
            name='extra_service',
            field=models.IntegerField(choices=[(0, 'NO EXTRA SERVICE'), (1, 'SEFETY INSPECTION'), (2, 'SEFETY INSPECTION +PLUS'), (3, 'COMPLETE SEFETY INSPECTION')], default=0),
        ),
        migrations.AlterField(
            model_name='bookingtime',
            name='check_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookingtime',
            name='check_time',
            field=models.IntegerField(choices=[(0, '07:00 - 07:30'), (1, '07:30 - 08:00'), (2, '08:00 - 08:30'), (3, '08:30 - 09:00'), (4, '09:00 - 09:30'), (5, '09:30 - 10:00'), (6, '10:00 - 10:30'), (7, '10:30 - 11:00'), (8, '11:00 - 11:30'), (9, '11:30 - 12:00'), (10, '12:00 - 12:30'), (11, '12:30 - 13:00'), (12, '13:00 - 13:30'), (13, '13:30 - 14:00'), (14, '14:00 - 14:30'), (15, '14:30 - 15:00'), (16, '15:00 - 15:30'), (17, '15:30 - 16:00'), (18, '16:00 - 16:30'), (19, '16:30 - 17:00'), (20, '17:00 - 17:30'), (21, '17:30 - 18:00'), (22, '18:00 - 18:30'), (23, '18:30 - 19:00')], default=0),
        ),
    ]