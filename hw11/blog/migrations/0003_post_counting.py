# Generated by Django 4.1 on 2024-11-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_updated_at_alter_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="counting",
            field=models.IntegerField(default=0),
        ),
    ]