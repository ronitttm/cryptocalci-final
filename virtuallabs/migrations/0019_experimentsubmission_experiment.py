# Generated by Django 4.2.11 on 2024-04-20 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtuallabs', '0018_experiments_remove_experimentsubmission_quiz_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentsubmission',
            name='experiment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='virtuallabs.experiments'),
        ),
    ]
