# Generated by Django 4.1 on 2024-11-02 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_counting"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="counting",
        ),
    ]
