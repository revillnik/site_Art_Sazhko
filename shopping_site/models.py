from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class goods(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )
    price = models.IntegerField(verbose_name="Цена")
    size = models.TextField(blank=True, verbose_name="Размер")
    content = models.TextField(blank=True, verbose_name="Описание")
    material = models.TextField(blank=True, verbose_name="Материал")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Главное фото на главной странице",
    )
    photos = models.ManyToManyField(
        "images",
        blank=True,
        related_name="photos",
        verbose_name="Фотографии в карточке товара",
    )
    cat = models.ForeignKey(
        "category",
        on_delete=models.SET_NULL,
        related_name="cats",
        verbose_name="Категории",
        null=True,
    )

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})


class images(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", default="Без названия"
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Фото",
    )

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.name


class category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    def __str__(self):
        return self.name
