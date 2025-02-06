from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from restaurants.models import Restaurant

class RestaurantModelTest(TestCase):
    def setUp(self):
        # Restaurant 모델 테스트에 필요한 설정
        self.restaurant_data = {
            'name': 'Test Restaurant',
            'address': '123 Test Street',
            'contact': '123-456-7890',
            'open_time': '09:00:00',
            'close_time': '21:00:00',
            'last_order': '20:30:00',
            'regular_holiday': 'MON'
        }

    def test_create_restaurant(self):
        # Restaurant 모델의 create 메서드 테스트
        restaurant = Restaurant.objects.create(
            name=self.restaurant_data['name'],
            address=self.restaurant_data['address'],
            contact=self.restaurant_data['contact'],
            open_time=self.restaurant_data['open_time'],
            close_time=self.restaurant_data['close_time'],
            last_order=self.restaurant_data['last_order'],
            regular_holiday=self.restaurant_data['regular_holiday']
        )

        # 레스토랑이 제대로 생성되었는지 확인
        self.assertEqual(restaurant.name, self.restaurant_data['name'])
        self.assertEqual(restaurant.address, self.restaurant_data['address'])
        self.assertEqual(restaurant.contact, self.restaurant_data['contact'])
        self.assertEqual(str(restaurant.open_time), self.restaurant_data['open_time'])
        self.assertEqual(str(restaurant.close_time), self.restaurant_data['close_time'])
        self.assertEqual(str(restaurant.last_order), self.restaurant_data['last_order'])
        self.assertEqual(restaurant.regular_holiday, self.restaurant_data['regular_holiday'])

class RestaurantViewTestCase(APITestCase):
    def setUp(self):
        # 테스트용 데이터 생성
        self.restaurant_data = {
            "name": "Test Restaurant",
            "address": "123 Test Street",
            "contact": "123-456-7890",
            "open_time": "09:00:00",
            "close_time": "21:00:00",
            "last_order": "20:30:00",
            "regular_holiday": "MON"
        }
        self.restaurant = Restaurant.objects.create(**self.restaurant_data)

    def test_restaurant_list_view(self):
        # 레스토랑 목록 조회 테스트
        url = reverse('restaurant-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_restaurant_post_view(self):
        # 레스토랑 생성 테스트
        url = reverse('restaurant-list')
        new_data = {
            "name": "New Restaurant",
            "address": "456 New Street",
            "contact": "987-654-3210",
            "open_time": "10:00:00",
            "close_time": "22:00:00",
            "last_order": "21:30:00",
            "regular_holiday": "TUE"
        }
        response = self.client.post(url, new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 2)

    def test_restaurant_detail_view(self):
        # 특정 레스토랑 조회 테스트
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.restaurant.name)

    def test_restaurant_update_view(self):
        # 레스토랑 정보 수정 테스트
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        updated_data = {
            "name": "Updated Restaurant",
            "address": self.restaurant.address,
            "contact": self.restaurant.contact,
            "open_time": self.restaurant.open_time,
            "close_time": self.restaurant.close_time,
            "last_order": self.restaurant.last_order,
            "regular_holiday": self.restaurant.regular_holiday
        }
        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.name, "Updated Restaurant")

    def test_restaurant_delete_view(self):
        # 레스토랑 삭제 테스트
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Restaurant.objects.count(), 0)
