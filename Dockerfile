# Multi-stage Dockerfile for production build (backend + frontend)

# --- Stage 1: build frontend assets ---
FROM node:18-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production
COPY frontend/ .
RUN npm run build

# --- Stage 2: build backend and assemble final image ---
FROM python:3.11-slim AS backend
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc g++ libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy backend application code
COPY backend/app/ ./app/
COPY backend/alembic/ ./alembic/

# Copy built frontend static assets
COPY --from=frontend-build /app/frontend/build ./app/static/

# Create uploads and logs directories
RUN mkdir -p app/uploads app/logs

# Environment variables
ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    ENVIRONMENT=production

# Expose application port
EXPOSE 8000

# Start service with Uvicorn/Gunicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000", "--workers", "4"]