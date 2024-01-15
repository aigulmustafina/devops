# usermod

Команда `usermod` проста и позволяет изменять параметры учетной записи. Для нее доступны многие параметры из тех, что используются с `useradd`.

### Полезное

- Введите команду `usermod` в терминале для получения списка всех флагов

### Задание

1. Измените учетную запись с именем пользователя `mark` на логин - `marktwain`
2. Установить другой пароль пользователю - `marktwain1835`.

---

### Ответ

```bash
$ sudo usermod -l "marktwain" mark
$ sudo passwd marktwain
Changing password for user marktwain.
New password: marktwain1835
Retype new password: marktwain1835
```
