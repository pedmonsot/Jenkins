FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --break-system-packages -r requirements.txt || true

CMD ["python3", "-m", "unittest", "discover"]

