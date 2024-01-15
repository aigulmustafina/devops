# mongo-install

### Полезное

- [Download MongoDB Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

### Задание

1. Установить на удаленном сервере stepik наиболее актуальную версию `mongodb`.
2. Запустить `mongodb`.
3. Создать пользователя-администратора с логин паролем `admin:singularity` и ролью `root`.
4. Перезагрузить сервис.

---

### Ответ

```bash
sudo apt update
sudo apt install -y gnupg
curl -sL https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod

sudo mongo << EOF
use admin
db.createUser(
  {
    user: "admin",
    pwd: "singularity",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
EOF
```
