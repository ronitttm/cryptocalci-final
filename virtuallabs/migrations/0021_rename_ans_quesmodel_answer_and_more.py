# Generated by Django 4.2.11 on 2024-04-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virtuallabs', '0020_quesmodel_experiment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quesmodel',
            old_name='ans',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op1',
            new_name='Option_1',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op2',
            new_name='Option_2',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op3',
            new_name='Option_3',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op4',
            new_name='Option_4',
        ),
    ]
