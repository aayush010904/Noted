from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_notes_users"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notes",
            old_name="users",
            new_name="user",
        ),
    ]