# Generated by Django 4.2.7 on 2024-02-06 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_user_expiration_date_alter_user_referral_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 2, 9, 25, 145307), verbose_name='Код действителен до'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(default=7540036, max_length=7, verbose_name='Ваш реферальный код'),
        ),
    ]
