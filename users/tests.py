from django.test import TestCase
from users.models import User
from django.db.utils import IntegrityError


class UserModelTest(TestCase):
    def setUp(self):
        # User 모델 테스트에 필요한 설정
        self.user_data = {
            'email': 'testuser@example.com',
            'nickname': 'testnickname',
            'password': 'testpassword'
        }

    def test_user_manager_create_user(self):
        # UserManager의 create_user 메서드 테스트
        user = User.objects.create_user(
            email=self.user_data['email'],
            nickname=self.user_data['nickname'],
            password=self.user_data['password']
        )

        # 유저가 제대로 생성되었는지 확인
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.nickname, self.user_data['nickname'])
        self.assertTrue(user.check_password(self.user_data['password']))

    def test_user_manager_create_superuser(self):
        # UserManager의 create_superuser 메서드 테스트
        superuser = User.objects.create_superuser(
            email=self.user_data['email'],
            nickname=self.user_data['nickname'],
            password=self.user_data['password']
        )

        # 슈퍼유저 생성 여부 확인
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.check_password(self.user_data['password']))

