FROM python:3.9-slim

WORKDIR /JenkinsPractice

COPY requisitos.txt /JenkinsPractice/

RUN pip install --no-cache-dir -r requisitos.txt

COPY src /JenkinsPractice/src

ENV PYTHONPATH=/JenkinsPractice/src

CMD ["python", "-m", "unittest", "discover", "-s", "src"]
