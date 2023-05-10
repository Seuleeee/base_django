# BASE Django Backend

* 프로젝트 마다 Django, Django Rest Framework, 각종 패키지 설치가 귀찮았습니다.
* DB 연동, Swagger Setting, Project Structure 변경이 힘들었습니다.
* 그리하여, Django - MariaDB - Redis 를 동시에 사용 가능한 Project Base를 만들었습니다.


## 적용 기술

[![Python 3.9](https://img.shields.io/badge/Python-3.9-informational?style=flat&logo=python&logoColor=white&color=blue)](https://www.python.org/downloads/release/python-390/)  
[![Django 4.1.4](https://img.shields.io/badge/Django-4.1.4-informational?style=flat&logo=django&logoColor=white&color=green)](https://docs.djangoproject.com/en/4.1/releases/4.1.4/)  
[![PostgreSQL 14](https://img.shields.io/badge/PostgreSQL-14-informational?style=flat&logo=postgresql&logoColor=white&color=blue)](https://www.postgresql.org/about/news/postgresql-14-released-2314/)
[![MariaDB 12](https://img.shields.io/badge/MariaDB-12-informational?style=flat&logo=mariadb&logoColor=white&color=blue)](https://mariadb.org/)  
[![Celery 5.2.7](https://img.shields.io/badge/Celery-5.2.7-informational?style=flat&logo=celery&logoColor=white&color=green)](https://docs.celeryproject.org/en/stable/index.html)
[![Redis](https://img.shields.io/badge/Redis-latest-informational?style=flat&logo=redis&logoColor=white&color=red)](https://redis.io/)


## 사용 방법
> **WARNING:** DataBase가 구축되어 있음을 가정합니다.

### Development
0. Clone
    ```shell
    git clone https://github.com/Seuleeee/base_django.git
    cd base_django
    ```

1. Package 설치
   - Linux / Mac
       ```shell
       python -m venv .venv
       source .venv/bin/activate
       python -m pip install --upgrade pip
       ```
  
   - Windows
       ```shell
       python -m venv .venv
       .venv\Scripts\activate
       python -m pip install --upgrade pip
       pip install -r requirements.txt 
       ```  

2. 환경 설정
   - .env 파일 추가 : config/settings/.env
       ```text
       SECRET_KEY="hashed secret key"
       DB_ENGINE=django.db.backends.postgresql or django.db.backends.mysql
       DB_NAME=db_name
       DB_USER=user
       DB_PASSWORD=user_password
       DB_HOST=localhost
       DB_PORT=3306

       EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
       EMAIL_HOST='smtp.gmail.com' (사용하는 HOST를 입력해주세요.)
       EMAIL_HOST_USER='example@gmail.com'
       EMAIL_HOST_PASSWORD='password'
       EMAIL_ADMIN='example@gmail.com'
       EMAIL_PORT=587
    
       CELERY_BROKER_URL='redis://localhost:6379/0'
       ```
   - logs/ 디렉토리 프로젝트 최상단 추가

3. 실행
   ```shell
    python .\manage.py runserver 0.0.0.0:8000
   ```
   
#### Production
1. 환경 설정
   - .env.prod 파일 추가 : config/settings/.env.prod
       ```text
       SECRET_KEY="hashed secret key"
       DB_ENGINE=django.db.backends.postgresql or django.db.backends.mysql
       DB_NAME=db_name
       DB_USER=user
       DB_PASSWORD=user_password
       DB_HOST=localhost
       DB_PORT=3306

       EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
       EMAIL_HOST='smtp.gmail.com' (사용하는 HOST를 입력해주세요.)
       EMAIL_HOST_USER='example@gmail.com'
       EMAIL_HOST_PASSWORD='password'
       EMAIL_ADMIN='example@gmail.com'
       EMAIL_PORT=587
    
       CELERY_BROKER_URL='redis://localhost:6379/0'
       ```

2. 실행
    ```shell
    docker compose up --build
    ```