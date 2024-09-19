from rest_framework import serializers

from .models import Cart, Category, Comment, Order, Product, Rating, Review


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user", "product", "cart", "quantity"]

    def create(self, validated_data):
        cart = Cart.objects.get(user=validated_data.get("user"))

        cart.total_price += validated_data.get("product").price * validated_data.get(
            "quantity"
        )
        cart.save()

        return Order.objects.create(**validated_data)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["user", "created_at", "total_price"]
