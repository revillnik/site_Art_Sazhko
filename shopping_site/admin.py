from django.contrib import admin
from .models import goods, images, category
from django.utils.safestring import mark_safe


@admin.register(goods)
class goodsAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "slug",
        "price",
        "size",
        "content",
        "material",
        "photo",
        "post_photo",
        "photos",
        "cat",
    ]
    readonly_fields = [
        "post_photo",
    ]
    search_fields = [
        "name__iregex",
    ]
    list_display = (
        "id",
        "name",
        "slug",
        "post_photo",
    )
    list_display_links = ("id", "name")
    ordering = [
        "name",
    ]
    filter_horizontal = ["photos"]
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 12

    @admin.display(description="Изображение")
    def post_photo(self, goods: goods):
        if goods.photo:
            return mark_safe(f"<img src='{goods.photo.url}' width=50>")
        return "Без фото"


@admin.register(images)
class imagesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo", "post_image")
    list_display_links = ("id", "name", "photo")
    list_per_page = 12
    fields = [
        "name",
        "photo",
        "post_image",
    ]
    search_fields = [
        "name__iregex",
    ]
    readonly_fields = [
        "post_image",
    ]

    @admin.display(description="Изображение")
    def post_image(self, images: images):
        if images.photo:
            return mark_safe(f"<img src='{images.photo.url}' width=100>")
        return "Без фото"


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_per_page = 12
    list_display = ("name", "slug")
    list_display_links = ("name", "slug")
    fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = [
        "name__iregex",
    ]
