# Use the official Python image as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    libpq-dev \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY CRPR/requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Create a non-root user and switch to it
#RUN useradd -m appuser
#USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Add a health check
#HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#    CMD curl -f http://localhost:8000/ || exit 1

RUN chmod +x ./CRPR/manage.py

# Run the application
CMD ["python", "./CRPR/manage.py", "runserver", "0.0.0.0:8000"]
