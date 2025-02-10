from django.contrib import admin
from .models import Restaurant  # 모델 가져오기

admin.site.register(Restaurant)  # 모델 등록