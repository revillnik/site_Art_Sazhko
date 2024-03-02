# Generated by Django 4.2.1 on 2024-03-02 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shopping_site", "0002_alter_category_options_alter_goods_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="comments",
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
                ("state", models.IntegerField(null=True, verbose_name="Оценка")),
                ("comment", models.TextField(blank=True, verbose_name="Комментарий")),
                (
                    "good",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="comment_good",
                        to="shopping_site.goods",
                        verbose_name="Товар",
                    ),
                ),
                (
                    "user",
                    models.ManyToManyField(
                        default="Неизвестный пользователь",
                        related_name="comment_users",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
    ]