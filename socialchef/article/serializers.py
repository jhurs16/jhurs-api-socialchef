from rest_framework import serializers
from user.models import Profile
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = '__all__'
