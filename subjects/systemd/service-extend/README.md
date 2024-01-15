# service-extend

### Полезное

- [Документация конфигурационного файла](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#[Unit]%20Section%20Options)

### Задание

1. Дается конфигурационный файл сервисного юнита, в который нужно дописать новые параметры.

```ini
[Unit]
Description=Jusan Management server

[Service]
ExecStart=/opt/jusan/server 8080
ExecReload=/opt/jusan/server -t
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
```

2. Добавить параметр, обязующий запускать сервис только после запуска сервисов `sshd.service`, `nginx.service`.
3. Добавить алиас `jusand.service`.
4. Добавить параметр запуска сервиса, если присутствует файл (см. "existence of a file") `/opt/jusan/server`.

---

### Ответ

```ini
[Unit]
Description=Jusan Management server
After=sshd.service nginx.service

[Service]
ExecStart=/opt/jusan/server 8080
ExecReload=/opt/jusan/server -t
ExecReload=/bin/kill -HUP $MAINPID
ConditionPathExists=/opt/jusan/server

[Install]
WantedBy=multi-user.target
Alias=jusand.service
```
