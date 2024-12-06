

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_remove_author_slug"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Author",
        ),
    ]