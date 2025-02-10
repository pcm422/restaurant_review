from django.contrib import admin
from .models import Review  # 모델 가져오기

admin.site.register(Review)  # 모델 등록