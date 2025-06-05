FROM python:3.10
WORKDIR /app
COPY etl.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "etl.py"]
