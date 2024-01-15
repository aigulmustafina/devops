# useradd-senior

### Задание

1. Создать учетную запись с именем пользователя `mark` и полным именем `Mark Twain`.
2. Установите оболочку по умолчанию (англ. "default shell", см. `флаг -s`) - `/bin/bash`.
3. Установите пользователю домашний каталог (см. `флаги -m,-d`) - `/home/marktwain`.
4. Установить основную группу, которой нет в системе (см. `флаг --user-group`) `mark`.
5. Установить уникальный идентификатор пользователя (прим. "user ID, UID", см. `флаг -u`) - 567
6. Установить дату устаревания учетной записи (англ. "expiration date", см. `флаг -e`) - 30.11.2035
7. Указать каталог с шаблоном (прим. "skeleton directory", см. `флаг -k`) - `/proc`
8. Добавить в группы (см. `флаг -G`) `bin` и `staff`.
9. Установить пароль пользователю `mark` - `S@wYer`.
10. Зайдите в систему как пользователь `mark` и создайте в домашнем каталоге файл `config.txt` с содержимым:

```
success: true
```

---

### Ответ

```bash
$ sudo useradd -c "Mark Twain" -s "/bin/bash" -G "bin,staff" -m -d "/home/marktwain" --user-group -u "567" -e "2035-11-30" -k "/proc" mark
$ sudo passwd mark
Changing password for user mark.
New password: S@wYer
Retype new password: S@wYer
$ sudo su -l mark
$ echo "success: true" > config.txt
```
