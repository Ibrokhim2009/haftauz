# Generated by Django 5.0.6 on 2025-04-11 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_new"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=130)),
                ("email", models.EmailField(max_length=100)),
                ("massege", models.TextField(verbose_name="Text")),
                ("is_trash", models.BooleanField(default=False)),
                ("is_read", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Sub",
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
                ("email", models.EmailField(max_length=254, verbose_name=120)),
                ("is_sub", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("user", models.CharField(max_length=139)),
                ("comments", models.TextField(verbose_name="Text")),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "news_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.new"
                    ),
                ),
            ],
        ),
    ]
