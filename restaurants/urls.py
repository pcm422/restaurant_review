from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

# DefaultRouter는 자동으로 url을 생성해준다.
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)  # 'restaurants/'에 대한 라우팅 처리

urlpatterns = [
    path('', include(router.urls)),  # URL들을 자동으로 포함시킨다.
]
