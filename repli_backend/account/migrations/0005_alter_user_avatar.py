# Generated by Django 5.0.4 on 2024-04-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_posts_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.jpg', null=True, upload_to='avatars'),
        ),
    ]