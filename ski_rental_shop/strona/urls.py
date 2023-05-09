from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>', views.detail, name='detail'),
    path('about', views.about, name='about'),
    path('user/<int:user_id>', views.user, name='user'),
    path('buy_page/<int:article_id>', views.buy_page, name='buy_page'),
    path('signup', views.sign_up, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.django_logout, name='logout'),
]
