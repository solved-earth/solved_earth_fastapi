FROM python:3.11

COPY Pipfile ./
COPY Pipfile.lock ./

RUN python -m pip install --upgrade pip
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app

COPY ./FastAPI/ /app
COPY ./yolov5/ /app

ADD run.sh ./

RUN chmod +x ./run.sh

CMD ["./run.sh"] 