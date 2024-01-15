# first-5

Подсказка:

- Команда `head` для показа первых строк в файле

### Задание

1. Написать скрипт, который покажет первые 5 линии из файла `./access.log`.

Файл `access.log` для примера:

```
80.91.33.133 - - [17/May/2015:08:05:50 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.22)"
173.203.139.108 - - [17/May/2015:08:05:03 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
80.91.33.133 - - [17/May/2015:08:05:35 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.16)"
5.83.131.103 - - [17/May/2015:08:05:51 +0000] "GET /downloads/product_1 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.22)"
80.91.33.133 - - [17/May/2015:08:05:59 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
200.6.73.40 - - [17/May/2015:08:05:42 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
80.91.33.133 - - [17/May/2015:08:05:48 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
```

---

### Ответ

```bash
head -n 5 ./access.log
```
