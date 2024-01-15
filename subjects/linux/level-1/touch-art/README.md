# touch-art

### Полезное

- Команда для создания ссылок `ln`
- Команда для создания папок `mkdir`

### Задание

1. В корневой директории создайте папку `touch-art` и создайте папки и файлы в `touch-art`, чтобы
   права, названия файлов, ссылок и папок был таким же как по примеру ниже.

Пример проверки прав:

```bash
$ cd touch-art
$ ls -lF
total 4
-rwxrwxrwx. 1 box box    0 Mar 28 08:22 a*
lrwxrwxrwx. 1 box box    1 Mar 28 08:22 b -> a*
-rw-----wx. 1 box box    0 Mar 28 08:22 c*
drw--w--wx. 2 box box 4096 Mar 28 08:22 d/
-rw--w--wx. 1 box box    0 Mar 28 08:22 e*
-rw-----wx. 1 box box    0 Mar 28 08:22 f*
-rwx---rwx. 1 box box    0 Mar 28 08:22 g*
-rwxrwxrwx. 1 box box    0 Mar 28 08:22 h*
```

---

### Ответ

```bash
mkdir touch-art && cd touch-art
touch a c e f g h
mkdir d
ln -s a b
chmod 707 g
chmod 777 a h
chmod 603 c f
chmod 623 d e
```
