
# Restaurant Review Project

## 프로젝트 개요

이 프로젝트는 사용자가 레스토랑에 대한 리뷰를 작성하고, 레스토랑 정보와 리뷰를 확인할 수 있는 웹 애플리케이션입니다. 이 애플리케이션은 Django와 Django Rest Framework를 사용하여 RESTful API로 구성되어 있으며, 레스토랑과 리뷰에 대한 CRUD(Create, Read, Update, Delete) 작업을 지원합니다.

## 주요 기능

- **레스토랑 등록 및 조회**: 레스토랑 정보(이름, 주소, 연락처 등)를 추가하고, 등록된 레스토랑 목록을 조회할 수 있습니다.
- **레스토랑 정보 수정 및 삭제**: 등록된 레스토랑의 정보를 수정하거나 삭제할 수 있습니다.
- **리뷰 작성 및 조회**: 사용자가 레스토랑에 대한 리뷰를 작성하고, 다른 사용자가 작성한 리뷰를 볼 수 있습니다.
- **사용자 인증**: 유저는 로그인 및 회원가입을 통해 서비스를 이용할 수 있습니다. (Django의 기본 인증 시스템 사용)

## 기술 스택

- **Backend**: Django, Django Rest Framework
- **Database**: MySQL (혹은 사용자가 설정한 다른 DB)
- **Authentication**: Django 기본 인증 시스템
- **Testing**: Django TestCase, DRF의 API TestCase

## 설치 방법

### 1. GitHub에서 프로젝트 클론

```bash
git clone https://github.com/yourusername/restaurant-review.git
cd restaurant-review
```

### 2. 가상 환경 설정 (선택 사항)

```bash
python3 -m venv venv
source venv/bin/activate  # Windows에서는 venv\Scriptsctivate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 설정

`config/settings.py` 파일에서 데이터베이스 설정을 확인하고 수정합니다. 기본적으로 MySQL을 사용합니다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oz_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 6. 슈퍼유저 생성 (관리자 계정 생성)

```bash
python manage.py createsuperuser
```

### 7. 서버 실행

```bash
python manage.py runserver
```

웹 애플리케이션은 `http://127.0.0.1:8000/`에서 실행됩니다.

## API 엔드포인트

- `GET /restaurants/` : 레스토랑 목록 조회
- `POST /restaurants/` : 레스토랑 등록
- `GET /restaurants/{id}/` : 특정 레스토랑 정보 조회
- `PUT /restaurants/{id}/` : 특정 레스토랑 정보 수정
- `DELETE /restaurants/{id}/` : 특정 레스토랑 삭제

## 테스트

프로젝트의 테스트는 `restaurants/tests.py`, `reviews/tests.py`, `users/tests.py` 파일에 정의되어 있습니다.

테스트 실행:

```bash
python manage.py test
```

## 기여 방법

1. 포크(fork) 후, 새로운 브랜치를 생성합니다.
2. 기능을 추가하거나 버그를 수정합니다.
3. 변경 사항을 커밋합니다.
4. 풀 리퀘스트(Pull Request)를 생성하여 기여합니다.

