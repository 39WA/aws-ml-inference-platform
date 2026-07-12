# ==============================
# Stage 1: Dependency builder
# ==============================
FROM python:3.12-slim AS builder

WORKDIR /build

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt


# ==============================
# Stage 2: Production runtime
# ==============================
FROM python:3.12-slim AS runtime

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libxcb1 \
       libglib2.0-0 \
       libgl1 \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

RUN groupadd --system appgroup \
    && useradd --system \
       --gid appgroup \
       --create-home \
       --home-dir /home/appuser \
       appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY --chown=appuser:appgroup . .

RUN mkdir -p /tmp/ultralytics \
    && chown -R appuser:appgroup /app /tmp/ultralytics

ENV YOLO_CONFIG_DIR=/tmp/ultralytics

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--timeout", "120", "wsgi:app"]
