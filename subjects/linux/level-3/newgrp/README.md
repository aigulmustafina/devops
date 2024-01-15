# newgrp

- Когда пользователь `john` создает файл или папку, по умолчанию они принадлежат основной группе `john`.
- Пользователь `john` может принадлежать к нескольким дополнительным группам или не принадлежать ни к одной. Если бы пользователь `john` был членом групп `finance` и `developer`, запись об этом отображалась бы в файле `/etc/group` следующим образом:

```
finance:x:908:sara,mike,murat,john
developer:x:909:serik,adil,john
```

- Пользователь не может добавить себя в дополнительную группу, как и включить другого пользователя в свою. Назначать пользователей в группы может только обладающий правами суперпользователя.

- Любой файл, назначенный группе `finance` или `developer`, доступен пользователю `john` с правами, установленными для группы. Если пользователь хочет создать файл с назначенными ему группами `finance` или `developer`, то он должен использовать команду `newgrp`. В этом примере `john` задействует команду `newgrp`, чтобы группа `finance` временно стала основной, и создает файл:

```bash
$ touch file1
$ ls -l file*
­rw­rw­r­­. 1 john john  0 Jan 18 22:22 file1
$ newgrp finance
$ touch file2
$ ls -l file*
­rw­rw­r­­. 1 john john  0 Jan 18 22:22 file1
­rw­rw­r­­. 1 john finance 0 Jan 18 22:23 file2
$ exit
```

### Задание

1. Создать учетную запись `john` c полным именем `John Cena`, с домашней директорией `/home/john` и паролем `myTimeIsNoW!`.
2. Установить основную группу (см. `флаг --user-group`) `john`.
3. Добавить в группу (см. `флаг -G`) `daemon`.
4. Зайдите в систему как пользователь `john` и временно назначьте группу `daemon` как основную.
5. Создайте в домашнем каталоге файл `config-daemon.txt` с содержимым `success: true`.
6. Временно назначьте группу `john` как основную.
7. Создайте в домашнем каталоге файл `config-john.txt` с содержимым `success: true`.

---

### Ответ

```bash
$ sudo useradd -c "John Cena" -m -G "daemon" --user-group john
$ sudo passwd john
Changing password for user john.
New password: myTimeIsNoW!
Retype new password: myTimeIsNoW!
$ sudo su -l john
$ newgrp daemon
$ echo "success: true" > config-daemon.txt
$ newgrp john
$ echo "success: true" > config-john.txt
```
