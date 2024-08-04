FROM python:3.10 AS builder

ENV ORIGIN=http://localhost:8080
WORKDIR /app

COPY . .
RUN \
    python -m pip install --upgrade \
      'pip==24.2' \
      'wheel==0.43.0' \
      'setuptools==72.1.0' && \
    pip install -r requirements.lock && \
    pip install -r requirements-dev.lock

CMD ["pytest"]
