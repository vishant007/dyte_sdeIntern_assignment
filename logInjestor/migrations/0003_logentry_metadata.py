# Generated by Django 4.1.7 on 2023-11-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logInjestor', '0002_rename_log_logentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='metadata',
            field=models.JSONField(blank=True, null=True),
        ),
    ]