# Generated by Django 5.0.4 on 2024-04-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_alter_comment_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postattachment",
            name="image",
            field=models.ImageField(
                default="post_attachments/default_image.jpg",
                upload_to="post_attachments",
            ),
        ),
    ]
