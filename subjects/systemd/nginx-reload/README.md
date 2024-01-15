# nginx-reload

### Задание

1. На сервере запущен сервис nginx. Проверьте его статус.
2. Добавьте файл `/etc/nginx/sites-enabled/server.conf` с содержимым:

```nginx
server {
    listen 9090;

    location / {
        return 200 'hello, from jusan-devops course!';
    }
}
```

Данный конфигурационный файл добавляет новый nginx-сервер на порту 9090. Однако, чтобы изменения
вступили силу нужно перезагрузить (англ. "reload") nginx.

3. Перезагрузите nginx.
4. Проверьте работоспособность нового сервера, сделав запрос `curl localhost:9090`. Ответ должен вернуть `hello, from jusan-devops course!`.
5. Посмотрите на логи nginx `sudo tail -f /var/log/nginx/access.log`

---

### Ответ

```bash
cat << EOF > /etc/nginx/conf.d/server.conf
server {
    listen 9090;

    location / {
        return "hello, from jusan-devops course!", 200;
    }
}
EOF
sudo service nginx reload
sudo service nginx status
curl localhost:9090
```
