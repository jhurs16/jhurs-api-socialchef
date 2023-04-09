
from django.shortcuts import render

# django_spectacular
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TipsandTrick
from .serializers import TipsTricksSerializer


class TipsTricksViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all articles
    """
    queryset = TipsandTrick.objects.all()

    @extend_schema(responses=TipsTricksSerializer)
    def list(self, request):
        serializer = TipsTricksSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ListTipsandTricks(APIView):

    """
    Tips and Tricks Lists
    """

    def get(self, request):
        
        query = TipsandTrick.objects.all()
        serializer = TipsTricksSerializer(query, many=True)

        return Response(serializer.data)
    
