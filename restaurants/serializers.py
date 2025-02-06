from rest_framework import serializers
from .models import Restaurant  # Restaurant 모델이 있어야 함

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'  # 모든 필드를 포함
