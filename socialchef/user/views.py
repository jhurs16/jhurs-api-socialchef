# django_spectacular
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer



class ListUsers(APIView):
    """
    Users Lists
    """
    def get(self, request):
        
        query = Profile.objects.all()
        serializer = ProfileSerializer(query, many=True)

        return Response(serializer.data)


class FeaturedUser(APIView):
    """
    Users Lists
    """
    def get(self, request):
        
        query = Profile.objects.filter(status="F")[:1]
        serializer = ProfileSerializer(query, many=True)

        return Response(serializer.data)

# class ListLatestRecipes(APIView):
#     """
#     Latest Recipe Lists
#     """
#     def get(self, request):
        
#         query = Recipe.objects.filter(stats="L").order_by("created")[:6]
#         serializer = RecipeSerializer(query, many=True)

#         return Response(serializer.data)
