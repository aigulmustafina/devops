FROM ubuntu:18.04

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt install -y gnupg2 curl

RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ bionic nginx" > /etc/apt/sources.list.d/nginx.list
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx" >> /etc/apt/sources.list.d/nginx.list
RUN curl -sLO http://nginx.org/keys/nginx_signing.key && apt-key add nginx_signing.key
RUN apt update && apt install -y nginx

RUN apt install -y software-properties-common && \
    add-apt-repository -y ppa:ondrej/php && \
    apt update
RUN apt install -y \
    git \
    php8.0 \
    php8.0-fpm \
    php8.0-common \
    php8.0-sqlite3 \
    php8.0-mysql \
    php8.0-gmp \
    php8.0-curl \
    php8.0-intl \
    php8.0-mbstring \
    php8.0-xmlrpc \
    php8.0-soap \
    php8.0-ldap \
    php8.0-gd \
    php8.0-bcmath \
    php8.0-xml \
    php8.0-cli \
    php8.0-zip
RUN mkdir -p /run/php

WORKDIR /app
RUN curl -sLO https://getcomposer.org/download/2.3.3/composer.phar && \
    mv composer.phar /usr/bin/composer && \
    chmod 755 /usr/bin/composer

RUN git clone https://github.com/wintercms/winter /var/www/winter

WORKDIR /var/www/winter
RUN composer install
RUN cat ./config/database.php | sed "s/'default' => 'mysql'/'default' => 'sqlite'/g" > ./config/database.php
RUN touch ./storage/database.sqlite && chmod 666 ./storage/database.sqlite
RUN php artisan winter:up

RUN rm /etc/nginx/conf.d/default.conf
COPY deploy-php.conf /etc/nginx/conf.d/deploy-php.conf
RUN echo "listen.owner = nginx" >> /etc/php/8.0/fpm/pool.d/www.conf
RUN echo "listen.group = nginx" >> /etc/php/8.0/fpm/pool.d/www.conf
RUN echo "user = nginx" >> /etc/php/8.0/fpm/pool.d/www.conf
RUN echo "group = nginx" >> /etc/php/8.0/fpm/pool.d/www.conf

COPY start.sh /start.sh
RUN chmod 755 /start.sh
RUN chown -R nginx:nginx /var/www/winter

ENTRYPOINT [ "/start.sh" ]
CMD [ "php-fpm8.0", "--nodaemonize" ]
