## Рецензия

### Дополнительная информация

<img src="../../../resources/code-review.png" alt="code-review.png" width="250"/>

Рецензия - это проверка проекта другого учащегося. Перед тем, как приступить к рецензированию, ознакомьтесь с правилами проведения рецензии.

**Правила рецензии:**

- Проверять только выполненную работу.
- Следовать указаниям критериев оценки.
- Если проект учащегося соответствует критерию, то ставьте 1.
- Если проект учащегося не соответствует критерию, то ставьте 0.

### Критерий оценки #1

GitHub ссылка рабочая и ведет на репозиторий с выполненным заданием.

Если это не так, то ставьте оценку 0 и заканчивайте проверку.

### Критерий оценки #2

В репозиторий добавлен файл `.gitignore`, который содержит [рекомендации](https://github.com/github/gitignore/blob/main/Python.gitignore).

### Критерий оценки #3

В репозиторий добавлен файл `requirements.txt`.

### Критерий оценки #4

В репозиторий добавлен файл `README.md`, который содержит инструкцию для запуска проекта, начиная с установки окружения.

### Критерий оценки #5

Запустите API.

Выполнение инструкции из `README.md` запускает проект без ошибок.

### Критерий оценки #6

Запросы на `/sum1n` выдает результат.

```bash
curl -i http://localhost:8000/sum1n/10
```

Обратите внимание на код статуса `HTTP/1.1 200 OK`

```http
HTTP/1.1 200 OK
date: Tue, 22 Mar 2022 10:38:09 GMT
server: uvicorn
content-length: 15
content-type: application/json

{"result":55}
```

```bash
curl http://localhost:8000/sum1n/20
```

```json
{ "result": 210 }
```

### Критерий оценки #7

Запросы на `/fibo` выдают результат.

```bash
curl -i http://localhost:8000/fibo?n=5
```

Обратите внимание на код статуса `HTTP/1.1 200 OK`

```http
HTTP/1.1 200 OK
date: Tue, 22 Mar 2022 10:39:23 GMT
server: uvicorn
content-length: 12
content-type: application/json

{"result":3}
```

```bash
curl http://localhost:8000/fibo?n=10
```

```json
{ "result": 34 }
```

### Критерий оценки #8

Запросы на `/reverse` выдают результат.

```bash
curl -X POST -H "string: hello" -i http://localhost:8000/reverse
```

Обратите внимание на код статуса `HTTP/1.1 200 OK`

```http
HTTP/1.1 200 OK
date: Tue, 22 Mar 2022 10:40:27 GMT
server: uvicorn
content-length: 18
content-type: application/json

{"result":"olleh"}
```

```bash
curl -X POST -H "string: jusan singularity" http://localhost:8000/reverse
```

```json
{ "result": "ytiralugnis nasuj" }
```

### Критерий оценки #9

Запросы на `/list` выдают результат.

```bash
curl -i http://localhost:8000/list
```

Обратите внимание на код статуса `HTTP/1.1 200 OK`

```http
HTTP/1.1 200 OK
date: Tue, 22 Mar 2022 10:41:43 GMT
server: uvicorn
content-length: 13
content-type: application/json

{"result":[]}
```

```bash
curl -X PUT -d '{"element":"Jusan"}' -H 'Content-Type: application/json' -i http://localhost:8000/list
```

Обратите внимание на код статуса `HTTP/1.1 200 OK`

```http
HTTP/1.1 200 OK
date: Tue, 22 Mar 2022 10:47:14 GMT
server: uvicorn
content-length: 4
content-type: application/json

null
```

Запустите еще раз, чтобы добавить элемент в массив.

```bash
curl -X PUT -d '{"element":"Singularity"}' -H 'Content-Type: application/json' http://localhost:8000/list
```

Проверим массив.

```bash
curl http://localhost:8000/list
```

```json
{ "result": ["Jusan", "Singularity"] }
```

### Критерий оценки #10

Запросы на `/calculator` выдают результат.

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "1,+,1"}' -i http://localhost:8000/calculator
```

Обратите внимание на код статуса `HTTP/1.1 200 OK`

```http
HTTP/1.1 200 OK
date: Tue, 22 Mar 2022 10:47:59 GMT
server: uvicorn
content-length: 12
content-type: application/json

{"result":2}
```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "125,+,143"}' http://localhost:8000/calculator
```

```json
{ "result": 268 }
```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "893,-,765"}' http://localhost:8000/calculator
```

```json
{ "result": 128 }
```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "9,\*,11"}' http://localhost:8000/calculator
```

```json
{ "result": 99 }
```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "125,\*,25"}' http://localhost:8000/calculator
```

```json
{ "result": 5 }
```

Следующие запросы должны вывести результат ниже.

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "word,\*,25"}' -i http://localhost:8000/calculator
```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "125,w,25"}' -i http://localhost:8000/calculator
```

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "125,/,w"}' -i http://localhost:8000/calculator
```

Ожидаемый результат. Обратите внимание на код статуса `HTTP/1.1 400 Bad Request`.

```http
HTTP/1.1 400 Bad Request
date: Tue, 22 Mar 2022 10:50:30 GMT
server: uvicorn
content-length: 19
content-type: application/json

{"error":"invalid"}
```

Проверка на деление на нуль.

```bash
curl -H "Content-Type: application/json" -X POST -d '{"expr": "125,/,0"}' -i http://localhost:8000/calculator
```

Обратите внимание на код статуса `HTTP/1.1 403 Bad Request`

```http
HTTP/1.1 403 Forbidden
date: Tue, 22 Mar 2022 10:51:45 GMT
server: uvicorn
content-length: 19
content-type: application/json

{"error":"zerodiv"}
```

### Критерий оценки #11

Импортируйте файл с коллекцией в Postman. Коллекция содержит следующие запросы.

- GET `/sum1n`
- GET `/fibo`
- POST `/reverse`
- PUT `/list`
- GET `/list`
- POST `/calculator`
- POST `/calculator` для проверки на статус 400
- POST `/calculator` для проверки на статус 403

### Критерий оценки #12

В следующих запросах во вкладке `Tests` есть тест на статус 200.

- GET `/sum1n`
- GET `/fibo`
- POST `/reverse`
- PUT `/list`
- GET `/list`
- POST `/calculator`

### Критерий оценки #13

Есть запрос POST `/calculator`, у которого во вкладке `Tests` есть тест на статус 400.

В другом запросе POST `/calculator` во вкладке `Tests` есть тест на статус 403.

### Критерий оценки #14

Запуск каждого запроса проходит успешно и во вкладке `Test Results` все тесты проходят успешно.
