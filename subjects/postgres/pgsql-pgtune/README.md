# pgsql-pgtune

PostgreSQL, как и nginx, имеет основной файл конфигурации, который отвечает
за внутренние параметры сервиса. Этих переменных очень много и уметь их
правильно настраивать под свои нужды является отдельным искуством.

Есть хороший ресурс [pgtune.leopard.in.ua](https://pgtune.leopard.in.ua/),
который подбирает оптимальные параметры конфигурации для того чтобы оптимизировать
базу данных под характеристики сервера, сложности и частоты запросов.

### Задание

1. Подберите параметры на [pgtune.leopard.in.ua](https://pgtune.leopard.in.ua/) под характеристики:
   - PostgreSQL 14
   - ОС: Linux
   - Тип БД: Обработка онлайн-транзакций
   - ОЗУ: 512 MB
   - ЦПУ: 2
   - Тип хранилища: SSD
2. Пришлите получившийся конфиг.

---

### Ответ

```conf
max_connections = 300
shared_buffers = 128MB
effective_cache_size = 384MB
maintenance_work_mem = 32MB
checkpoint_completion_target = 0.9
wal_buffers = 3932kB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 436kB
min_wal_size = 2GB
max_wal_size = 8GB
max_worker_processes = 2
max_parallel_workers_per_gather = 1
max_parallel_workers = 2
max_parallel_maintenance_workers = 1
```
