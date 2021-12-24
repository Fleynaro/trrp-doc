
# docker build --progress=plain -t docker-labcode3 .

FROM python:3.7

RUN mkdir /server
WORKDIR /server

COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY ./grpc ./grpc
COPY ./shared ./shared

COPY ./config.py ./
COPY ./services/document/ ./

EXPOSE 50051
ENTRYPOINT ["python", "./main.py"]