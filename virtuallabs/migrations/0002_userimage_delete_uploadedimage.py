# Generated by Django 4.2.6 on 2023-10-31 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtuallabs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]
