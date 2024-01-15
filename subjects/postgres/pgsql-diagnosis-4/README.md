# pgsql-diagnosis-4

### Задание

1. Пришлите названия колонок через новую линию в БД `deadline` в таблице `student_deadline` на сервере `pgsql-commands` в `postgres`.

---

### Ответ

```
\d+ student_deadline
```

```
id
student_id
deadline_id
module_id
index
duration
is_success
started_at
created_at
updated_at
```
