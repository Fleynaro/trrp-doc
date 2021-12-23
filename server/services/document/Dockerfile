# СБОРКА
# docker build --progress=plain -t docker-labcode3 .

# ЗАПУСК
# docker run docker-labcode3 train - тренировка сети на датасете mnist
# docker run docker-labcode3 train test - проверка на тестовом датасете mnist
# docker run docker-labcode3 test [путь к картинке или к директории с картинками]

FROM python:3.7

RUN mkdir /server
WORKDIR /server
ADD . /server/

RUN python -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

EXPOSE 50051
ENTRYPOINT ["python", "/server/start_dispatcher.py"]