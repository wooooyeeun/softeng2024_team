# Generated by Django 4.1 on 2024-12-06 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_delete_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
    ]