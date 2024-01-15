# nginx-stop

### Задание

1. На сервере запущен сервис nginx. Проверьте его статус.
2. Остановите сервис nginx.
3. Проверьте статус сервиса nginx.
4. Проверьте работоспособность nginx, сделав запрос `curl localhost`
5. Посмотрите на логи nginx `sudo tail -f /var/log/nginx/access.log`

---

### Ответ

```bash
sudo service nginx status
sudo service nginx stop
sudo service nginx status
curl localhost
sudo tail -f /var/log/nginx/access.log
```
