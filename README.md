﻿# BASE Django Backend

* 프로젝트 마다 Django, Django Rest Framework, 각종 패키지 설치가 귀찮았습니다.
* DB 연동, Swagger Setting, Project Structure 변경이 힘들었습니다.
* 그리하여, Django - MariaDB - Redis 를 동시에 사용 가능한 Project Base를 만들었습니다.


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

## Environment Varialbles
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
* 생성 위치 : config/.env
* django 환경 변수 세팅
```
SECRET_KEY=settings.py 에 default 로 생성되어있는 secret_key 를 옮긴 값
DEBUG=True

DB_ENGINE=django.db.backends.mysql
DB_NAME={생성 할 DB명, 따옴표 불필요}
DB_USER={생성 할 user명, 따옴표 불필요}
DB_PASSWORD={생성 할 user password, 따옴표 불필요}
DB_HOST=maraidb # docker-compose.yml 에서 지정한 container_name
DB_PORT=3306
```

## 실행 방법
* docker-compose 사용 가능 환경
* docker-compose.yml 파일이 위치한 경로에서 아래 명령어를 입력
```
docker-compose up --build
```
