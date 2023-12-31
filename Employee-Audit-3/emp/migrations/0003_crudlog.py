# Generated by Django 4.2.6 on 2023-10-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emp", "0002_department_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="CRUDLog",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("action", models.CharField(max_length=10)),
                ("model", models.CharField(max_length=100)),
                ("object_id", models.PositiveIntegerField()),
                ("details", models.TextField()),
            ],
        ),
    ]
