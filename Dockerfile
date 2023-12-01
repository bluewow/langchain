# 베이스 이미지로 파이썬 공식 이미지 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install sse_starlette

# 애플리케이션 파일 복사
COPY . .

# 애플리케이션 실행을 위한 포트 설정
EXPOSE 8000

# 애플리케이션 실행 명령어
CMD ["python", "serve.py"]
