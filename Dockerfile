FROM python:3.9-slim

WORKDIR /app

COPY requisitos.txt /app/

RUN pip install --no-cache-dir -r requisitos.txt

COPY src /app/src

ENV PYTHONPATH=/app/src

CMD ["python", "-m", "unittest", "discover", "-s", "src"]
