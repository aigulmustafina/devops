# mongo-backup

### Полезное

- [mongodump](https://www.mongodb.com/docs/database-tools/mongodump/)

### Задание

1. На сервере установлен `mongodb`. Учетная запись администратора - `admin:singularity`.
   В `mongodb` поднята база данных `reservations`. Можете проверить подключение:

```bash
mongo -u "admin" -p "singularity" --authenticationDatabase admin
```

2. Создайте бэкап базы данных `reservations` и заверните его в архив `/home/box/reservations-dump.tar.gz`.
3. Вывод файлов в архиве должен быть следующим:

```bash
$ tar -tf /home/box/reservations-dump.tar.gz
reservations/
reservations/user_reservations.bson
reservations/rooms.metadata.json
reservations/user_reservations.metadata.json
reservations/users.bson
reservations/users.metadata.json
reservations/rooms.bson
```

---

# backup

```bash
mongodump --db reservations -u admin -p singularity --authenticationDatabase admin
tar -zcvf reservations-dump.tar.gz reservations
```
