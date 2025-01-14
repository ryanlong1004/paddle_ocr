FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git wget ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app
CMD ["python", "main.py"]
