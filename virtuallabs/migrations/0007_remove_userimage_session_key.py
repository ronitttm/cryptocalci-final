# Generated by Django 4.2.5 on 2023-11-04 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virtuallabs', '0006_code_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='session_key',
        ),
    ]
