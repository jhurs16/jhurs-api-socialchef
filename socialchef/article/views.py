
from django.shortcuts import render

# django_spectacular
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all articles
    """
    queryset = Article.objects.all()

    @extend_schema(responses=ArticleSerializer)
    def list(self, request):
        serializer = ArticleSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ListArticles(APIView):

    """
    Article Lists
    """

    def get(self, request):
        
        query = Article.objects.all()
        serializer = ArticleSerializer(query, many=True)

        return Response(serializer.data)
    
class ListLatestArticles(APIView):
    """
    Latest Recipe Lists
    """
    def get(self, request):
        
        query = Article.objects.filter(stats="L").order_by("created")[:6]
        serializer = ArticleSerializer(query, many=True)

        return Response(serializer.data)
    
