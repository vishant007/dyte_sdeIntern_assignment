# Generated by Django 4.1.7 on 2023-11-17 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logInjestor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Log',
            new_name='LogEntry',
        ),
    ]
