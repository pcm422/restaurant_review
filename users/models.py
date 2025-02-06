from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


def user_profile_image_path(instance, filename):
    # 이미지 저장 경로: users/profile_images/filename
    return f'users/profile_images/{filename}'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("이메일은 꼭 필요해!")
        if not nickname:
            raise ValueError("닉네임은 꼭 필요해!")

        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(email, nickname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    profile_image = models.ImageField(
        upload_to=user_profile_image_path,
        default='users/blank_profile_image.png'
    )

    # 추가적으로 is_active, is_staff 등의 필드가 필요함
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email
