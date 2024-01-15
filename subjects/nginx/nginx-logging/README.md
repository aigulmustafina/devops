# nginx-logging

Логирование — это основа понимания вашего приложения. С NGINX у вас есть полный контроль над важной логируемой информацией.

В nginx ошибки записываются в `/var/log/nginx/error.log`, а успешные запросы в `/var/log/nginx/access.log`.

Часто чтобы посмотреть на последние логи, запускают команду:

```bash
tail /var/log/nginx/error.log
```

Эта команда покажет лог 10 последних ошибок.

### Задание

1. На сервере запущен nginx, но в нем есть ошибка. Найдите эту ошибку и устраните ее, чтобы nginx работал как следует.

Ожидается, что при запросе на `localhost` вернется следующий ответ:

```bash
$ curl localhost
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

---

### Ответ

```nginx
cat << EOF > /etc/nginx/conf.d/default.conf
server {
    listen       80;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }
}
EOF
```
