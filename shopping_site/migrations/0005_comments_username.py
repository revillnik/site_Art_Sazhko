# Generated by Django 4.2.1 on 2024-03-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopping_site", "0004_alter_comments_good_remove_comments_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="username",
            field=models.TextField(blank=True, verbose_name="Материал"),
        ),
    ]
