# Generated by Django 4.1 on 2024-11-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="file_upload",
            field=models.FileField(blank=True, upload_to="blog/files/%Y/%m/%d"),
        ),
    ]
