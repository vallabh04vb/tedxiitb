# Generated by Django 4.2.1 on 2023-07-25 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedapp', '0003_rename_roll_useraccount_refferal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='refferal',
            new_name='referral',
        ),
    ]