from rest_framework import serializers
from .models import Review, Recipe

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'name', 'email', 'review', 'priority')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'dish_name', 'recipe')
