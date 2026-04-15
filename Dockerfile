# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the app with Gunicorn for production-ready deployment
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]