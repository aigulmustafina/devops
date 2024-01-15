# none-type

Прогуглите как исправить ошибку:

```
TypeError: 'NoneType' object is not subscriptable
```

Исходный код программы Python:

```python
numbers = [3, 2, 1]
output = numbers.sort()

print(output[0])
```

Прислать исправленный код.

> P.S. В этом задании не важно, знаете ли вы Python. Главное, чтобы вы научились находить решение для проблем, даже тех, в которых вы не разбираетесь.

---

### Ответ

Код:

```python
numbers = [3, 2, 1]
numbers.sort()

print(numbers[0])
```

Вывод:

```
1
```
