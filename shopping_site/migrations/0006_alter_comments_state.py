# Generated by Django 4.2.1 on 2024-03-02 21:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopping_site", "0005_comments_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="state",
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="Оценка",
            ),
        ),
    ]
