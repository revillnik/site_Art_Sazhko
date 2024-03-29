# Generated by Django 4.2.1 on 2024-02-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopping_site", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категорию", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="goods",
            options={"verbose_name": "Изделие", "verbose_name_plural": "Изделия"},
        ),
        migrations.AlterModelOptions(
            name="images",
            options={"verbose_name": "Фотографию", "verbose_name_plural": "Фотографии"},
        ),
        migrations.AlterField(
            model_name="goods",
            name="photo",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="photos/%Y/%m/%d/",
                verbose_name="Главное фото на главной странице 370x450",
            ),
        ),
        migrations.AlterField(
            model_name="goods",
            name="photos",
            field=models.ManyToManyField(
                blank=True,
                related_name="photos",
                to="shopping_site.images",
                verbose_name="Фотографии в карточке товара 570x693",
            ),
        ),
    ]
