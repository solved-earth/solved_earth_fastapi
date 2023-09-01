FROM python:3.11

COPY Pipfile ./
COPY Pipfile.lock ./

RUN python -m pip install --upgrade pip
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install pipenv && pipenv install --dev --system --deploy

COPY ./FastAPI/ /app
COPY ./yolov5/ /app

WORKDIR /app/FastAPI

CMD ["cd", "FastAPI", "&&", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 