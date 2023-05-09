import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Brand(models.Model):
    brand_name = models.CharField(max_length=70)
    articles_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.brand_name


class Article(models.Model):
    SKI = 'SKI'
    SKI_BOOTS = 'BOOTS'
    SKI_POLES = 'POLES'
    HELMET = 'HELMET'
    GOGGLES = 'GOGGLES'
    SNOWBOARD = 'SNOWBOARD'
    type_choices = [
        (SKI, 'SKI'),
        (SKI_BOOTS, 'SKI_BOOTS'),
        (SKI_POLES, 'SKI_POLES'),
        (HELMET, 'HELMET'),
        (GOGGLES, 'GOGGLES'),
        (SNOWBOARD, 'SNOWBOARD'),
    ]
    name = models.CharField(max_length=130)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=10, choices=type_choices, default=SKI)
    number_available = models.PositiveIntegerField(default=0)
    test = models.CharField(max_length=10, default='aaa')
    image = models.ImageField(upload_to='', default='default.png')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_orders = models.IntegerField(default=0)
    birth_date = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.username


class Orders(models.Model):
    article = models.CharField(default='', max_length=130)
    article_price = models.IntegerField(default=0)
    delivery = models.BooleanField(default=False)
    order_address = models.CharField(max_length=150, default='')
    number_of_articles = models.PositiveIntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    order_date = models.DateField(default=datetime.date.today)
    customer = models.ForeignKey(Profile, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

