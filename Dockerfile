# 베이스 이미지 선택
FROM python:3.9.3

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 추가
COPY . /app/

# 실행 명령 지정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]