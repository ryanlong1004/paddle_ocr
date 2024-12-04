# Use a base image with Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create a working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget 'http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb' && dpkg -i 'libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb'

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && python -m src.main --help

# Specify the command to run the script
ENTRYPOINT ["python", "-m", "src.main"]
