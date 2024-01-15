# second-touch

### Полезное

- [Изменение прав с помощью chmod](https://younglinux.info/bash/chmod)
- Команда `chmod`
- Команда `ls`
- [Understanding Linux File Permissions](https://linuxize.com/post/understanding-linux-file-permissions/)

### Задание

1. В корневой директории `/home/box` создать файл с названием `second` и с текстом внутри `touch`.
2. Установить созданному файлу права `rw--wx-w-`.

Пример проверки прав:

```bash
$ ls -l
-rw--wx-w-  1 root  staff    6 Mar  7 16:23 second
```

---

### Ответ

```bash
echo "touch" > second
chmod 632 second
```
