from django import template
from django.db.models import Count
from shopping_site.models import category, goods
from shopping_site import views

register = template.Library()


@register.inclusion_tag("shopping_site/list_categories.html")
def show_categories(cat_slug):
    categories = category.objects.all()
    return {"categories": categories, "cat_slug": cat_slug}
