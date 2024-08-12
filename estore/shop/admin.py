from django.contrib import admin
from .models import Category
from .models import Product
from .models import Order
from .models import Comment
from .models import Rating
from .models import Review
from .models import SampleModel

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(SampleModel)

