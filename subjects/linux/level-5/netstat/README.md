# netstat

Используя команду `netstat`, в выводе вы увидите процессы, которые прослушивают порты.

Запустите от имени суперпользователя, чтобы увидеть `PID` и название программы `Program name`.

```bash
$ sudo netstat -tupln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      88592/sshd
tcp        0      0 0.0.0.0:8088            0.0.0.0:*               LISTEN      68131/python
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      121934/postgres
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      1262/master
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      113832/nginx: worke
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      113832/nginx: worke
```

### Полезное

- Чтобы понять назначение флагов, запустите `man netstat`.

### Задание

1. Запустите у себя `netstat -tupln`.
2. Найдите сервис который работает на порту `53`.
3. Отправьте название программы (англ. "Program name") этого сервиса.

---

### Ответ

```
systemd-resolve
```
