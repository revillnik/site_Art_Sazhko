from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse, reverse_lazy

urlpatterns = [
    path("", views.SiteHome.as_view(), name="home"),
    path("product/<slug:product_slug>/", views.Product_details.as_view(), name="product"),
    path("shop/", views.Shop.as_view(), name="shop"),
    path("category/<slug:cat_slug>/", views.Categories.as_view(), name="category"),
    path("search/", views.search, name="search"),
    path("email/", views.email, name="email"),
    path("email_home/", views.email_home, name="email_home"),
    path("contact_with_us/", views.contact_with_us, name="contact_with_us"),
    path("contact/", views.Contact.as_view(), name="contact"),
]
