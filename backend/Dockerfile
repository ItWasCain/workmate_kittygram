FROM python:3.11.9-alpine3.20
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "workmate_kittygram.wsgi"]