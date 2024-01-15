# apt-source-nginx

В этом уроке установим nginx из официального репозитория разработчика.

### Полезное

- [официальный nginx инструкция](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-debian-package-from-the-official-nginx-repository)

### Задание

1. Обновите (англ. "update") базу пакетов.
2. Установить (англ. "install") nginx из официального репозитория.

Подсказки:

1. Чтобы узнать `CODENAME`

```bash
cat /etc/os-release
```

---

### Ответ

```bash
sudo bash -c 'cat << EOF > /etc/apt/sources.list.d/nginx.list
deb https://nginx.org/packages/ubuntu/ bionic nginx
deb-src https://nginx.org/packages/ubuntu/ bionic nginx
EOF'
sudo apt remove -y nginx-common
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ABF5BD827BD9BF62
sudo apt update
sudo apt install -y nginx
```
