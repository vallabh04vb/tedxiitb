# Generated by Django 4.2.1 on 2023-07-11 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='UserAccount',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='city',
            new_name='City',
        ),
    ]
