from authentication.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

    def apply_discount(self):
        if self.total_price > 20000:
            self.total_price *= 0.85
        elif self.total_price > 10000:
            self.total_price *= 0.90


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="comments", on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="ratings", on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
