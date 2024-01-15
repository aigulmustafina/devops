# grep

### Полезное

- Команда `grep` для поиска в текста

### Задание

1. Написать скрипт, который покажет в файле `./access.log` только линии содержащие `jusan.kz`.

Файл `access.log` для примера:

```
180.179.174.219 - - [17/May/2015:18:05:22 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 339 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
152.90.220.18 - - [17/May/2015:18:05:18 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 336 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
10.16.62.10 - - [17/May/2015:18:05:32 +0000] "GET http://example.com/downloads/product_1 HTTP/1.1" 404 318 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)"
180.179.174.219 - - [17/May/2015:18:05:52 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 336 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
62.210.152.199 - - [17/May/2015:18:05:38 +0000] "GET https://jusan.kz/downloads/product_1 HTTP/1.1" 200 2592 "-" "urlgrabber/3.9.1 yum/3.2.29"
204.77.169.137 - - [17/May/2015:18:05:23 +0000] "GET https://jusan.kz/downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.2)"
94.23.21.169 - - [17/May/2015:18:05:07 +0000] "GET http://example.com/downloads/product_1 HTTP/1.1" 404 328 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
85.214.47.178 - - [17/May/2015:18:05:08 +0000] "GET http://example.com/downloads/product_1 HTTP/1.1" 404 331 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
176.58.26.49 - - [17/May/2015:18:05:37 +0000] "GET https://jusan.kz/downloads/product_1 HTTP/1.1" 200 2575 "-" "urlgrabber/3.9.1 yum/3.2.29"
54.194.93.59 - - [17/May/2015:18:05:33 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 333 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)"
204.77.169.137 - - [17/May/2015:18:05:09 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 319 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.2)"
54.183.135.30 - - [17/May/2015:18:05:50 +0000] "GET https://jusan.kz/downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)"
204.77.169.137 - - [17/May/2015:18:05:46 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 319 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.2)"
202.78.200.137 - - [17/May/2015:18:05:12 +0000] "GET http://example.com/downloads/product_2 HTTP/1.1" 404 333 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)"
194.76.107.17 - - [17/May/2015:18:05:53 +0000] "HEAD /downloads/product_2 HTTP/1.1" 200 0 "-" "Wget/1.13.4 (linux-gnu)"
212.83.167.232 - - [17/May/2015:18:05:38 +0000] "GET http://example.com/downloads/product_1 HTTP/1.1" 404 341 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"
```

---

### Ответ

```bash
cat ./access.log | grep "jusan\.kz"
```
