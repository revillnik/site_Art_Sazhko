from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
)
from django.shortcuts import get_object_or_404
from .models import goods, comments
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class SiteHome(ListView):
    template_name = "shopping_site/index.html"
    context_object_name = "all_products"
    paginate_by = 6

    def get_queryset(self):
        return goods.objects.all()


class Product_details(DetailView):
    template_name = "shopping_site/product_details.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        return get_object_or_404(goods.objects, slug=self.kwargs[self.slug_url_kwarg])

    def post(self, request, *args, **kwargs):
        user = request.POST.get("user")
        username = request.POST.get("username")
        comment = request.POST.get("comment")
        state = request.POST.get("state")
        product = request.POST.get("product")
        comments.objects.create(
            state=state,
            comment=comment,
            good_id=product,
            user_id=user,
            username=username,
        )
        if request.POST.get("delete_buttom"):
           
        return redirect("product", self.kwargs.get("product_slug"))


class Shop(ListView):
    template_name = "shopping_site/product-left-sidebar.html"
    context_object_name = "all_products"
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_slug"] = "all_cat"
        return context

    def get_queryset(self):
        return goods.objects.all()


class Contact(TemplateView):
    template_name = "shopping_site/contact.html"


class Categories(ListView):
    template_name = "shopping_site/product-left-sidebar.html"
    context_object_name = "all_products"
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_slug"] = self.kwargs["cat_slug"]
        return context

    def get_queryset(self):
        return goods.objects.filter(cat__slug=self.kwargs["cat_slug"])


def search(request):
    search = request.POST.get("search")
    if request.POST.get("search"):
        products = goods.objects.filter(name__iregex=search)
        paginator = Paginator(products, 9)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        objects = page_obj.object_list
        return render(
            request,
            "shopping_site/product-left-sidebar.html",
            {
                "all_products": objects,
                "paginator": paginator,
                "page_obj": page_obj,
                "search_value": search,
            },
        )
    else:
        products = goods.objects.all()
        paginator = Paginator(products, 9)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        objects = page_obj.object_list
        return render(
            request,
            "shopping_site/product-left-sidebar.html",
            {
                "all_products": objects,
                "paginator": paginator,
                "page_obj": page_obj,
                "search_value": search,
            },
        )


def email(request):
    order_url = request.META["HTTP_REFERER"]
    email = request.POST["email"]
    if request.POST["email"]:
        send_mail(
            "Оформление заказа",
            f"Ссылка на изделие: {order_url}, номер телефона покупателя: {email}",
            settings.EMAIL_HOST_USER,
            ["revillnik@mail.ru"],
        )
    return redirect(request.META["HTTP_REFERER"], permanent=True)


def email_home(request):
    email = request.POST["email"]
    if request.POST["email"]:
        send_mail(
            "Запрос на связь от покупателя",
            f"Номер телефона покупателя: {email}",
            settings.EMAIL_HOST_USER,
            ["revillnik@mail.ru"],
        )
    return redirect(request.META["HTTP_REFERER"], permanent=True)


def contact_with_us(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    phone = request.POST["phone"]
    message = request.POST["message"]
    if request.POST["phone"]:
        send_mail(
            "Запрос на связь от покупателя",
            f"Покупатель: {first_name} {last_name},\nНомер телефона для связи: {phone},\nСообщение: {message}",
            settings.EMAIL_HOST_USER,
            ["revillnik@mail.ru"],
        )
    return redirect(request.META["HTTP_REFERER"], permanent=True)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "shopping_site/register.html"
    success_url = "login"


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "shopping_site/login.html"

    def get_success_url(self):
        return reverse_lazy("home")
