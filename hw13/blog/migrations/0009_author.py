
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_post_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=200, unique=True),
                ),
            ],
        ),
    ]