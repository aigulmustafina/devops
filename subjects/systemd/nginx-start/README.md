# nginx-start

### Задание

1. На сервере установлен сервис nginx, но он не запущен. Проверьте его статус.
2. Запустите сервис nginx.
3. Проверьте статус сервиса nginx.
4. Проверьте работоспособность nginx, сделав запрос `curl localhost`
5. Посмотрите на логи nginx `sudo tail -f /var/log/nginx/access.log`

---

### Ответ

```bash
sudo service nginx status
sudo service nginx start
sudo service nginx status
curl localhost
sudo tail -f /var/log/nginx/access.log
```
