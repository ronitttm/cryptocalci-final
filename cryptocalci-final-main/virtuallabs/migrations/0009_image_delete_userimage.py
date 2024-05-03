# Generated by Django 4.2.11 on 2024-03-20 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('virtuallabs', '0008_remove_code_session_key_userimage_session_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.BinaryField()),
                ('session_key', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('filename', models.CharField(max_length=255)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtuallabs.code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]
