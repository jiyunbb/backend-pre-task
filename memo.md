### 실행은 이렇게 해보셔도 좋을 것 같습니다. (docker-compose 이용)
- docker-compose로 요구사항에 맞는 실행환경(django, mysql DB)을 구성하였습니다. 필요하시면 실행시켜서 바로 사용해보실 수 있습니다.
  - 실행방법은 아래와 같습니다.
    1. 터미널을 통해 docker-compose 파일이 있는 경로로 이동합니다.
    2. `docker-compose up` 명령어를 통해 도커 환경을 띄웁니다.
       - mysql 관련 참고: DDL은 따로 실행시킬 필요 없이 docker가 띄워지는 경우 자동으로 sql 파일을 마운트하여 init 하도록 하였습니다. 최소한의 필요한 데이터 입력도 같이 실행되기 때문에 굳이 데이터 입력을 신경쓰지 않으셔도 됩니다.
       - django 관련 참고: mysql db가 정상 동작 할 때 까지 django는 DB 접근 오류가 날 수 있어서 django 컨테이너는 재시작 해주시면 20초 이내로 연결이 붙습니다.
         - 재시작 하는 방법
           - docker desktop을 이용하여 재시작 동작
           - pycharm 개발 툴로 docker-compose 파일의 django 서비스에서 재시작버튼 누르기
           - 터미널에서 `docker restart <컨테이너ID/이름>` 명령어 사용
         - 완료가 되면 콘솔 아래와 같은 내용들 뜸.
       ```
            (0.004) SHOW FULL TABLES; args=None
            Watching for file changes with StatReloader
            Performing system checks...
            System check identified no issues (0 silenced).
            (0.001) 
                            SELECT VERSION(),
                                   @@sql_mode,
                                   @@default_storage_engine,
                                   @@sql_auto_is_null,
                                   @@lower_case_table_names,
                                   CONVERT_TZ('2001-01-01 01:00:00', 'UTC', 'UTC') IS NOT NULL
                        ; args=None
            (0.001) SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; args=None
            (0.003) SHOW FULL TABLES; args=None
            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            March 31, 2024 - 15:04:14
            Django version 3.2.20, using settings 'conf.settings'
            Starting development server at http://0.0.0.0:8000/
            Quit the server with CONTROL-C.
       ```
    3. django가 띄워지면 `http://localhost:8000/` 으로 호출이 가능합니다. 자세한 api 스펙은 `openapi.yml` 참고 부탁드립니다.
    4. 포스트맨을 사용하신다면 "kidsnote.postman_collection.json" 파일을 동일한 디렉토리 내에 두었으니 import 후 사용하셔도 됩니다. 


### 이후에 개선해보면 좋을 것들.
1. 삭제 로직 만든다고 하면 soft delete로 설계 (DB 컬럼에 deleted_at을 추가) 하고 deleted_at이 비어있는 케이스만 조회하도록 model manager 사용하면 좋을 것 같다.
2. 지금은 단순한 형태라 유저테이블을 하나로 고려했지만 이후 확장성 생각하면 유저테이블 분리해도 좋을 것 같음.
3. Exception 내 detail 문구가 더 다양해진다면 공통화해도 좋을 것 같음.
4. 테스트 코드 미작성
