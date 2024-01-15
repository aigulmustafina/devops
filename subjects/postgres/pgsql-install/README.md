# pgsql-install

### Полезное

- [Download PostgreSQL Ubuntu](https://www.postgresql.org/download/linux/ubuntu/)

### Задание

1. Установить и запустить на удаленном сервере stepik наиболее актуальную версию `postgresql`.

---

### Ответ

```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
service postgresql start
```
