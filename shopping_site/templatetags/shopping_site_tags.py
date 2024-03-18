from django import template
from django.db.models import Count
from shopping_site.models import category, goods
from shopping_site import views

register = template.Library()


@register.inclusion_tag("shopping_site/list_categories.html")
def show_categories(cat_slug):
    categories = category.objects.annotate(count=Count("cats")).filter(count__gt=0)
    return {"categories": categories, "cat_slug": cat_slug}


@register.simple_tag(name="state_comment")
def get_state_comment(state):
    range_state = []
    if state > 0:
        for i in range(1, state + 1):
            range_state.append(i)
    else:
        range_state.append(0)
    while len(range_state) < 5:
        range_state.append(0)
    return range_state
