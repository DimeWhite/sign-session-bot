FROM python:3.12.10

WORKDIR /app/src

COPY requirements.txt .
COPY src/ /app/src

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]