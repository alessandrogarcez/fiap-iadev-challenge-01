FROM python:3.14.10-slim

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY main.py .python-version ./
COPY notebooks/ notebooks/

CMD ["python", "main.py"]
