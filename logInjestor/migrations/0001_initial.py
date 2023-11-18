# Generated by Django 4.1.7 on 2023-11-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('resourceId', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField()),
                ('traceId', models.CharField(max_length=20)),
                ('spanId', models.CharField(max_length=20)),
                ('commit', models.CharField(max_length=20)),
                ('parentResourceId', models.CharField(max_length=20)),
            ],
        ),
    ]