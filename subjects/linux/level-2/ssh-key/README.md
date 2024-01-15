# ssh-key

В этом уроке разберем как работать с удаленным сервером по `ssh`.

Для выполнения задачи нам понадобится запустить локальный VPS сервер. На компьютере должен быть установлен `docker`.

В терминале выполним следующую команду для запуска VPS:

```bash
PORT=22 && docker run -d --rm --name local-vps-$PORT -p $PORT:$PORT atlekbai/local-vps $PORT
```

Для подключения:

```bash
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@127.0.0.1 -p 22
```

Пароль: `password`

### Полезные ссылки

- [Установка ssh ключей](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804)

### Задание

1. Сгенерируйте связку ключей, если нет.
2. Установите ключи на VPS сервере, чтобы подключаться без пароля.
3. Выполненные команды отправьте в поле ввода.

---

### Ответ

```bash
ssh-keygen
ssh-copy-id root@127.0.0.1
```
