from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer

# ✅ 레스토랑 API를 위한 ModelViewSet (GET, POST, PUT, DELETE 지원)
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()  # 전체 레스토랑 데이터
    serializer_class = RestaurantSerializer  # 직렬화 클래스
