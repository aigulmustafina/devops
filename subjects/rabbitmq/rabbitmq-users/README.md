# rabbitmq-users

### Задание

На сервере установлен RabbitMQ. В этом задании нужно создать пользователей и вхосты.

1. Создать пользователя `administrator` с паролем `Lhc9kkVV`.
2. Создать пользователя `app-developer` с паролем `9cDtdMTj`.
3. Поменять пароль пользователю `guest` на `GmBtuC5X`
4. Создать vhost `application` и дать полные права пользователям `administrator` и `app-developer`.

---

### Ответ

```bash
sudo rabbitmqctl add_user administrator Lhc9kkVV
sudo rabbitmqctl add_user app-developer 9cDtdMTj
sudo rabbitmqctl change_password guest GmBtuC5X
sudo rabbitmqctl add_vhost application
sudo rabbitmqctl set_permissions -p application administrator ".\*" ".\*" ".\*"
sudo rabbitmqctl set_permissions -p application app-developer ".\*" ".\*" ".\*"
```
