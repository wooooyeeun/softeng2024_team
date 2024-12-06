
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="slug",
        ),
    ]