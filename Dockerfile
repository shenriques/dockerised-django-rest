FROM python:3.11-slim

# dont write .pyc files to disk, reduce I/O operations
ENV PYTHONDONTWRITEBYTECODE=1
# print to console without buffering = real time logging when app runs
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/newportfolio

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
