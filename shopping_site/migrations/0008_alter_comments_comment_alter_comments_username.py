# Generated by Django 4.2.1 on 2024-03-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopping_site", "0007_alter_comments_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="comment",
            field=models.TextField(blank=True, null=True, verbose_name="Комментарий"),
        ),
        migrations.AlterField(
            model_name="comments",
            name="username",
            field=models.TextField(blank=True, null=True, verbose_name="Материал"),
        ),
    ]
