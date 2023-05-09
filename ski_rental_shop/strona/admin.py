from django.contrib import admin
from .models import Brand, Article, Orders, Profile

admin.site.register(Brand)
admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Orders)
