# OCR Model

## Installing locally

```
pip install -r requirements.txt
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Deployement

### CPU commands

```
docker build -t graymeta/gm_ocr_v2:cpu -t graymeta/gm_ocr_v2:v0.1.3-cpu -f docker/Dockerfile.cpu .
docker run -p 8000:8000 -e VERSION="v0.1.0" -it graymeta/gm_ocr_v2:cpu
```

### GPU commands

```
docker build -t graymeta/gm_ocr_v2:gpu -t graymeta/gm_ocr_v2:v0.1.3-gpu -f docker/Dockerfile.gpu .
docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -p 8000:8000 -e VERSION="v0.1.0" -it graymeta/gm_ocr_v2:gpu
```

### Tagging and deploying

```
docker login
docker push graymeta/gm_ocr_v2:v0.1.0-cpu

(change cpu to gpu for gpu version)
```
