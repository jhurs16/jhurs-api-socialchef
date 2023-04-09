from rest_framework import serializers
from .models import TipsandTrick

class TipsTricksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipsandTrick 
        fields = '__all__'
