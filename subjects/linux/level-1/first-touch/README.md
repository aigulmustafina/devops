# first-touch

### Полезное

- [Статья: создание файлов в linux](https://linuxize.com/post/create-a-file-in-linux/)
- Команда `touch`
- Команда `echo`

### Задание

1. В корневой директории `/home/box` создать файл с названием `jusan` и с текстом внутри `singularity`.

Пример для проверки:

```bash
$ cat jusan
singularity
```

---

### Ответ

```bash
echo "singularity" > jusan
```
