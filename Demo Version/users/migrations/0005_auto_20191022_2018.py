# Generated by Django 2.2.6 on 2019-10-23 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191022_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='staff',
            new_name='is_staff',
        ),
    ]
