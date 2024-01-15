# mongo-restore

### Полезное

- [mongorestore](https://www.mongodb.com/docs/database-tools/mongorestore/)

### Задание

1. На сервере установлен `mongodb`. Учетная запись администратора - `admin:singularity`.
   Можете проверить подключение:

```bash
mongo -u "admin" -p "singularity" --authenticationDatabase admin
```

2. Поднимите [бэкап базы данных](https://stepik.org/media/attachments/lesson/705682/mongo-dump.tar.gz)
   в БД с именем `reservations`.

---

# backup

```bash
curl -sL https://stepik.org/media/attachments/lesson/705682/mongo-dump.tar.gz -o /home/box/mongo-dump.tar.gz
tar -xvf /home/box/mongo-dump.tar.gz -C /home/box

mongorestore -u "admin" -p "singularity" --authenticationDatabase admin -d reservations /home/box/reservations
```
