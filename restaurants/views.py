from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer