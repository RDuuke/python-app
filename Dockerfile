FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]