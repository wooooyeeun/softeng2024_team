# Generated by Django 4.1 on 2024-12-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]
