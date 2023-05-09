from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from strona.models import Orders


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Required')
    last_name = forms.CharField(max_length=50, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class OrderForm(forms.ModelForm):
    article = forms.CharField(max_length=130, disabled=True)
    article_price = forms.IntegerField(disabled=True)

    class Meta:
        model = Orders
        fields = ('article', 'article_price', 'delivery', 'order_address', 'number_of_articles', 'amount_paid')
