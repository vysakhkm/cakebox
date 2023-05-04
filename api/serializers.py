from django.contrib.auth.models import User
from cake.models import Cakes,Carts,Orders,Reviews
from rest_framework import serializers

class Usercreate(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields=["user","cake","comment","rating"]
    
class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cake_reviews=ReviewSerializer(read_only=True,many=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Cakes
        fields=["id","cake","image","name","price","weight","description","cake_reviews"]

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["user","status","qty","created_date","cake"]

class OrderSerializer(serializers.ModelSerializer):
    cake=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_deliverydate=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=["cake","user","created_date","status","expected_deliverydate","address","matter"]
