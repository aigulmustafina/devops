FROM ubuntu:18.04

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt install -y gnupg2 git

RUN apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.10 python3-pip

RUN python3 -m pip install --upgrade pip

RUN git clone https://github.com/django-ve/django-helloworld /app
WORKDIR /app
RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
