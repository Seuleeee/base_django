# BASE Django Backend

* 프로젝트 마다 Django, Django Rest Framework, 각종 패키지 설치가 귀찮았습니다.
* DB 연동, Swagger Setting, Project Structure 변경이 힘들었습니다.
* 그리하여, Django - MariaDB - Redis 를 동시에 사용 가능한 Project Base를 만들었습니다.

## Tech
## 적용 기술
<div>
 <img src="https://img.shields.io/badge/Python 3.11.1-3776AB?style=flat-square&logo=Python&logoColor=white"/>
 <img src="https://img.shields.io/badge/Django 4.1.4-092E20?style=flat-square&logo=Django&logoColor=white"/>
</div>
<div>
  <img src="https://img.shields.io/badge/MariaDB 10.7.3-003545?style=flat-square&logo=MariaDB&logoColor=white"/>
</div>
<div>
 <img src="https://img.shields.io/badge/Docker 20.10.17-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
</div>

## Structure
```
├─api
│  ├─migrations
│  ├─dao
│  ├─services
│  └─admin.py
│  └─apps.py
│  └─models.py
│  └─tests.py
│  └─urls.py
│  └─views.py
│  
├─config
│  └─.env (별도 작성 필요, 아래 참고)
│  └─asgi.py
│  └─settings.py
│  └─urls.py
│  └─wsgi.py
│
├─db
│  ├─conf.d
│  └───my.cnf
│  ├─data
│  └─initdb.d
|
└─.compose_env (별도 작성 필요, 아래 참고)
└─docker-compose.yml
└─Dockerfile.yml
```

## Environment Variables
### .compose_env
* 생성 위치 : 프로젝트 최상단
* docker-compose.yml 파일의 services > mariadb > environment 필드에 대응
```
MARIADB_PORT=3306
MARIADB_ROOT_PASSWORD={password 입력, 따옴표 불필요}
MARIADB_DATABASE={생성 할 DB명, 따옴표 불필요}
MARIADB_USER={생성 할 user명, 따옴표 불필요}
MARIADB_PASSWORD={생성 할 user password, 따옴표 불필요}
```

### .env
* 생성 위치 : config/settings/.env
* django 환경 변수 세팅
* Dev / Prod 분리하여 관리
```
SECRET_KEY=settings.py 에 default 로 생성되어있는 secret_key 를 옮긴 값

# ========== DEVELOPMENT ==========
DEV_DB_ENGINE=django.db.backends.mysql
DEV_DB_NAME={DB_NAME}
DEV_DB_USER={DB_USER}
DEV_DB_PASSWORD={DB_PASSWORD}
DEV_DB_HOST={DB_HOST}
DEV_DB_PORT=3306

# ========== PRODUCTION ==========
PROD_DB_ENGINE=django.db.backends.mysql
PROD_DB_NAME={DB_NAME}
PROD_DB_USER={DB_USER}
PROD_DB_PASSWORD={DB_PASSWORD}
PROD_DB_HOST=maraidb # docker-compose.yml 에서 지정한 container_name
PROD_DB_PORT=3306
```

## 실행 방법
* Production
  * docker-compose 사용 가능 환경
  * Swagger 적용 : 프로젝트 최상단 'static' 디렉토리 생성
  * docker-compose.yml 파일이 위치한 경로에서 아래 명령어를 입력
```
python manage.py collectstatic
docker-compose up --build
```

* Devlopment
  * 개발 환경, Local 실행
```
python manage.py collectstatic
python manage.py runserver
```

## 참고
* Table Not exist error
  * 테스트용으로 api/models 경로에 Board Model을 생성하여 발생
  * Solution 1 : 생성한 DB에 BOARD 테이블 생성
  * Solution 2 : Board 관련 기능 제거 후 build