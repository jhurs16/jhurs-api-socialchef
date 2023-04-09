from rest_framework import serializers
from user.models import Profile
from .models import (
    Recipe,
    RecipeCategory,
    Comment, 
    NutritionFact
)

class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory 
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = '__all__'


class NutritionFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionFact 
        exclude = ("id","recipe")

class RecipeSerializer(serializers.ModelSerializer):
    nutrition_fact = NutritionFactSerializer(many=True)
    class Meta:
        model = Recipe 
        fields = (
            "id",
            "name",
            "description",
            "featured_image",
            "cooking_time",
            "difficulty_level",
            "serves",
            "category",
            "ingredients",
            "procedure",
            "stats",
            "likes",
            "posted_by",
            "created",
            "nutrition_fact"
        )
