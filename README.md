# Paddle_OCR

Paddle_OCR is an Optical Character Recognition (OCR) tool developed using PaddlePaddle, a deep learning framework. It is designed to recognize and extract text from images, supporting multiple languages and various text detection and recognition models. Paddle_OCR is suitable for applications such as document digitization, automated data entry, and text extraction from images.

## Requirements

Install paddlepaddle

```bash
# cpu

python -m pip install paddlepaddle==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# gpu，该命令仅适用于 CUDA 版本为 11.8 的机器环境

python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# gpu，该命令仅适用于 CUDA 版本为 12.3 的机器环境

python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
```

Install paddlex

```bash
pip install paddlex==3.0.0b2
```

## Running the Application

### Using Docker

Build the Docker image:

```bash
docker build -t wasabiair/ocr_v3 -f Dockerfile .
```

Run the Docker container:

```bash
docker run --rm -v $(pwd):/app/temp wasabiair/ocr_v3 input.image_path=/app/temp/[IMAGE_NAME]
```
