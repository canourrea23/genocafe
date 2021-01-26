from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product, Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'username', 'email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image')


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'id', 'email', 'image', 'user', 'description', 'user'
        )

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.description = validated_data.get(
            'discription', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
