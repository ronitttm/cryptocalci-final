# Generated by Django 4.2.11 on 2024-04-19 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('virtuallabs', '0014_quizscore_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('code', models.TextField()),
                ('image', models.URLField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]