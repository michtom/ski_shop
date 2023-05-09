# from django.shortcuts import render
import datetime

from django.http import HttpResponse
from .models import Article, Orders, Profile, Brand
from .forms import SignUpForm
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    articles_sort_alphabetical = Article.objects.all().order_by('name')
    if request.GET.get("brand_choose") != "All" and request.GET.get("brand_choose") is not None:
        brand_instance = Brand.objects.get(brand_name=request.GET.get("brand_choose"))
        articles_sort_alphabetical = articles_sort_alphabetical.filter(brand=brand_instance)
    all_brands = Brand.objects.all().order_by('brand_name')
    template = loader.get_template('strona/index.html')
    context = {
        'articles_sort_alphabetical': articles_sort_alphabetical,
        'all_brands': all_brands,
    }
    return HttpResponse(template.render(context, request))


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    template = loader.get_template('strona/article_details.html')
    context = {'article': article}
    return HttpResponse(template.render(context, request))


def about(request):
    context = {}
    template = loader.get_template('strona/about.html')
    return HttpResponse(template.render(context, request))


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            username = user.username
            raw_password = form.cleaned_data.get('password1')
            user_profile = authenticate(username=username, password=raw_password)
            login(request, user_profile)
            messages.info(request, "Successfully created a new account.")
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'strona/signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="strona/login.html", context={"login_form": form})


def user(request, user_id):
    cur_user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=cur_user)
    user_orders = Orders.objects.filter(customer=profile).order_by('-order_date')
    context = {'profile': profile, 'user_orders': user_orders}
    template = loader.get_template('strona/user.html')
    return HttpResponse(template.render(context, request))


def django_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")


def buy_page(request, article_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        order = Orders()
        order.order_date = datetime.date.today()
        if request.POST.get('delivery') == 'on':
            order.delivery = True
            order.order_address = request.POST.get('address_value')
        else:
            order.delivery = False
            order.order_address = 'Company Address, 11-111 Example City'
        order.article_price = request.POST.get('price')
        order.number_of_articles = request.POST.get('items_number')
        order.amount_paid = request.POST.get('money_amount')
        order.article = request.POST.get('article_name')
        cur_user = request.user
        cur_profile = Profile.objects.get(user=cur_user)
        order.customer = cur_profile
        article = Article.objects.get(pk=article_id)
        article.number_available = article.number_available - int(order.number_of_articles)
        cur_profile.number_of_orders += 1
        cur_profile.save()
        article.save()
        order.save()
        messages.info(request, "Successfully bought an article.")
        return redirect('index')
    article = Article.objects.get(pk=article_id)
    range_number = range(1, article.number_available + 1)
    context = {'article': article, 'range_number': range_number}
    return render(request, template_name='strona/buy_page.html', context=context)
