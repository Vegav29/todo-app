# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*
RUN pip install gunicorn
# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run collectstatic during build
RUN python manage.py collectstatic --noinput

# Expose the port your app runs on
EXPOSE 8000

# Command to start the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]

