
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY temperature-api.py .


CMD ["python", "temperature-api.py"]
