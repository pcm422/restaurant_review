from django.test import TestCase
from reviews.models import Review
from users.models import User
from restaurants.models import Restaurant

class ReviewModelTest(TestCase):
    def setUp(self):
        # Review 모델 테스트에 필요한 설정
        self.user = User.objects.create_user(
            email='testuser@example.com',
            nickname='testnickname',
            password='testpassword'
        )
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test Street',
            contact='123-456-7890',
            open_time='09:00:00',
            close_time='21:00:00',
            last_order='20:30:00',
            regular_holiday='MON'
        )
        self.review_data = {
            'user': self.user,
            'restaurant': self.restaurant,
            'title': 'Great Food!',
            'comment': 'The food was amazing, would visit again.'
        }

    def test_create_review(self):
        # Review 모델의 create 메서드 테스트
        review = Review.objects.create(
            user=self.review_data['user'],
            restaurant=self.review_data['restaurant'],
            title=self.review_data['title'],
            comment=self.review_data['comment']
        )

        # 리뷰가 제대로 생성되었는지 확인
        self.assertEqual(review.user, self.review_data['user'])
        self.assertEqual(review.restaurant, self.review_data['restaurant'])
        self.assertEqual(review.title, self.review_data['title'])
        self.assertEqual(review.comment, self.review_data['comment'])
