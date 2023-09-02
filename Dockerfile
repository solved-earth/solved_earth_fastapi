FROM python:3.11

COPY Pipfile ./
COPY Pipfile.lock ./

RUN apt-get update && apt-get -y install libgl1-mesa-glx
RUN python -m pip install --upgrade pip
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app

COPY ./FastAPI/ /app/FastAPI
COPY ./yolov5/ /app/yolov5

ADD run.sh /app

RUN chmod +x ./run.sh

CMD ["/app/run.sh"] 