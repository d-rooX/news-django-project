# Generated by Django 2.2.24 on 2021-11-09 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news_api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="upvotes",
        ),
        migrations.CreateModel(
            name="Upvote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="upvotes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="upvotes",
                        to="news_api.Post",
                    ),
                ),
            ],
        ),
    ]
