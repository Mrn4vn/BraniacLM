# Generated by Django 3.2.23 on 2024-03-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_data_migration"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="courseteachers",
            options={"verbose_name": "Teacher", "verbose_name_plural": "Teachers"},
        ),
        migrations.AlterModelOptions(
            name="lesson",
            options={"ordering": ("course", "num"), "verbose_name": "Lesson", "verbose_name_plural": "Lessons"},
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"ordering": ("-created",), "verbose_name": "News", "verbose_name_plural": "News"},
        ),
    ]