# Use a small Python base image
FROM python:3.12-slim

# Don't buffer Python output
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (optional but useful)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Fly will set PORT, default to 8080
ENV PORT=8080

# Expose the port (just documentation)
EXPOSE 8080

# Start the app using gunicorn
# "backend:app" = from backend.py import app
CMD gunicorn backend:app --bind 0.0.0.0:${PORT}
