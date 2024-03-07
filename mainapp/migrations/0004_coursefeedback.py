# Generated by Django 5.0.3 on 2024-03-07 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_auto_20240306_1900"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseFeedback",
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
                (
                    "feedback",
                    models.TextField(default="No feedback", verbose_name="Feedback"),
                ),
                (
                    "rating",
                    models.SmallIntegerField(
                        choices=[
                            (5, "⭐⭐⭐⭐⭐"),
                            (4, "⭐⭐⭐⭐"),
                            (3, "⭐⭐⭐"),
                            (2, "⭐⭐"),
                            (1, "⭐"),
                        ],
                        default=5,
                        verbose_name="Rating",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                ("deleted", models.BooleanField(default=False)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.courses",
                        verbose_name="Course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
    ]
