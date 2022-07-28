from rest_framework import serializers
from . import models
from .models import Order, Channel, Brand_branch, Fp_branch, Order_Item, Item, Order_item_add_ons, Add_ons, Fp


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class fpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fp
        fields = '__all__'

class Fp_branchSerializer(serializers.ModelSerializer):
    fp = fpSerializer(many=False)
    class Meta:
        model = Fp_branch
        fields = '__all__'


class Brand_branchSerializer(serializers.ModelSerializer):
    Fp_branch = Fp_branchSerializer(many=False)
    class Meta:
        model = Brand_branch
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class Add_onsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_ons
        fields = '__all__'

class OrderItemAddOnesSerializer(serializers.ModelSerializer):
    Add_ons = Add_onsSerializer(many=False)
    class Meta:
        model = Order_item_add_ons
        fields = '__all__'

class Order_ItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False)
    order_item_add_ones = OrderItemAddOnesSerializer(many=False)
    class Meta:
        model = Order_Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(many=False)
    brand_branch = Brand_branchSerializer(many=False)
    order_Item = Order_ItemSerializer(many=False)
    class Meta:
        model = Order
        fields = '__all__'

#
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'
#
#
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
#
#
# class ProjectSerializer(serializers.ModelSerializer):
#     owner = ProfileSerializer(many=False)
#     tags = TagSerializer(many=True)
#     reviews = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#     def get_reviews(self, obj):
#         reviews = obj.review_set.all()
#         serializer = ReviewSerializer(reviews, many=True)
#
#         return serializer.data
#