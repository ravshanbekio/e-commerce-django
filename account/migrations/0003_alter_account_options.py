# Generated by Django 4.0.5 on 2022-06-16 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'Admin & Users'},
        ),
    ]
