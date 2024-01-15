# groupadd

Суперпользователь может создавать группы из командной строки с помощью команды `groupadd`.

### Полезное

- Введите команду `groupadd` в терминале для получения списка всех флагов

### Задание

1. Создайте группу `kings`.
2. Создать учетную запись `john` c полным именем `John Cena`, с домашней директорией `/home/john` и паролем `myTimeIsNoW!`.
3. Установить основную группу (см. `флаг --user-group`) `john`.
4. Добавьте `john` в дополнительную группу `kings`.
5. Зайдите в систему как пользователь `john`.
6. Создайте в домашнем каталоге файл `config-john.txt` с содержимым `success: true`.
7. Временно назначьте группу `kings` как основную.
8. Создайте в домашнем каталоге файл `config-kings.txt` с содержимым `success: true`.

---

### Ответ

```bash
$ sudo groupadd kings
$ sudo useradd -c "John Cena" -p "myTimeIsNoW!" --user-group -G "kings" john
$ sudo passwd john
Changing password for user john.
New password: myTimeIsNoW!
Retype new password: myTimeIsNoW!
$ sudo su -l john
$ echo "success: true" > config-john.txt
$ newgrp kings
$ echo "success: true" > config-kings.txt
```
