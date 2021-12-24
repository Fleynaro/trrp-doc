
# docker build --progress=plain -t docker-labcode3 .

FROM python:3.7

WORKDIR /server

RUN python -m pip install --upgrade pip setuptools
RUN pip install jupyter

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8888
ENTRYPOINT ["bash", "-c", "jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root"]