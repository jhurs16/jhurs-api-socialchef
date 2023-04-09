
from django.shortcuts import render

# django_spectacular
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe, Comment, RecipeCategory, NutritionFact
from .serializers import RecipeSerializer, CommentSerializer, RecipeCategorySerializer, NutritionFactSerializer



class ListRecipes(APIView):
    """
    Recipe Lists
    """
    def get(self, request):
        
        query = Recipe.objects.all()
        serializer = RecipeSerializer(query, many=True)

        return Response(serializer.data)


class ListLatestRecipes(APIView):
    """
    Latest Recipe Lists
    """
    def get(self, request):
        
        query = Recipe.objects.filter(stats="L").order_by("created")[:6]
        serializer = RecipeSerializer(query, many=True)

        return Response(serializer.data)


class FeaturedRecipe(APIView):
    """
    Recipe of the day.
    """
    def get(self, request):
        
        query = Recipe.objects.filter(stats="R")[:1]
        serializer = RecipeSerializer(query, many=True)

        return Response(serializer.data)
