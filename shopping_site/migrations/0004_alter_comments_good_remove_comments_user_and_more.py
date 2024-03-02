# Generated by Django 4.2.1 on 2024-03-02 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shopping_site", "0003_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="good",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comment_good",
                to="shopping_site.goods",
                verbose_name="Товар",
            ),
        ),
        migrations.RemoveField(
            model_name="comments",
            name="user",
        ),
        migrations.AddField(
            model_name="comments",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comment_users",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
