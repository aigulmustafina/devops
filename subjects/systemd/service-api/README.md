# service-api

В этом задании вам нужно запустить бинарник, т.е. программу, как systemd процесс. Бинарник представляет собой
API сервер, который запускается на порту 9090.

Данное задание нужно выполнить на компьютере с Linux. Можете использовать свой компьютер с Ubuntu.

### Задание

1. Задание выполняется в GitHub Classroom. После выполнения пришлите свою ссылку на рецензию ревьюеру в Stepik ([ССЫЛКА GITHUB CLASSROOM])
2. Создайте файл `api.service`, который будет содержать конфигурационный файл сервисного юнита. Такой, что:
   - Имеет описание `Description=API server`
   - Имеет алиас `Alias=api.service`
   - Запускает бинарник
3. Создайте файл `setup.sh`, который будет содержать команды для установки бинарника как systemd процесс.
4. Прислать ссылку на репозиторий.

Чтобы скачать бинарник введите команду.

```bash
curl -LO https://github.com/jusan-singularity/track-devops-systemd-api/releases/download/v0.1/api
```

Обязательно, чтобы бинарник запускался через systemd нужно дать ему права 755.

```bash
chmod 755 ./api
```

Файл `setup.sh` должен после запуска полноценно установить программу как systemd процесс без никаких дополнительных
действий от пользователя, кроме введения пароля суперпользователя.

Пример `setup.sh` файла.

```bash
cd /tmp # можно tmp для удобства
curl -LO https://github.com/jusan-singularity/track-devops-systemd-api/releases/download/v0.1/api
chmod 755 api
... # какие-то команды для настройки
sudo systemctl start api
```

После успешного установления системы, можете проверить работоспособность следующими путями.

### Проверка состояния сервиса

```bash
sudo systemctl status api
```

```bash
● api.service - API server
   Loaded: loaded (/lib/systemd/system/api.service; disabled; vendor preset: enabled)
   Active: active (running) since Wed 2022-03-16 11:52:34 UTC; 1min 8s ago
 Main PID: 58453 (api)
    Tasks: 4 (limit: 7003)
   Memory: 1.8M
   CGroup: /system.slice/api.service
           └─58453 /tmp/api

Mar 16 11:52:34 app-02 systemd[1]: Started API server.
```

### Проверка работы сервиса

```bash
$ curl localhost:9090
web-server: 0
$ curl localhost:9090
web-server: 1
$ curl localhost:9090
web-server: 2
```

---

### Ответ

```bash
cd /tmp # необязательно в tmp, главное чтобы в .service файле был указан путь
curl -LO https://github.com/jusan-singularity/track-devops-systemd-api/releases/download/v0.1/api
chmod 755 api
sudo bash -c 'cat << EOF > /lib/systemd/system/api.service
[Unit]
Description=API server

[Service]
ExecStart=/tmp/api
ConditionPathExists=/tmp/api

[Install]
WantedBy=multi-user.target
Alias=api.service
EOF'
sudo systemctl start api
```

Проверка состояния сервиса:

```bash
sudo systemctl status api
```

```bash
● api.service - API server
   Loaded: loaded (/lib/systemd/system/api.service; disabled; vendor preset: enabled)
   Active: active (running) since Wed 2022-03-16 11:52:34 UTC; 1min 8s ago
 Main PID: 58453 (api)
    Tasks: 4 (limit: 7003)
   Memory: 1.8M
   CGroup: /system.slice/api.service
           └─58453 /tmp/api

Mar 16 11:52:34 app-02 systemd[1]: Started API server.
```

Проверка работы сервиса:

```bash
$ curl localhost:9090
web-server: 0
$ curl localhost:9090
web-server: 1
$ curl localhost:9090
web-server: 2
```
