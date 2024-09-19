from django.contrib import admin

from .models import Cart, Category, Comment, Order, Product, Rating, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Cart)
