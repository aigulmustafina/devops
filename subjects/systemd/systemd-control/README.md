# systemd-control

Теперь, когда вы можете проверить состояние юнита, нужно научиться управлять службами на Linux:

- запускать
- останавливать
- перезагружать

Рассмотрим управление сервисом на примере юнита `nginx`.

### Остановка службы

<table>
<tr><td>systemctl</td><td>service</td></tr>
<tr>
<td>

```bash
systemctl stop nginx
```

</td>
<td>

```bash
service nginx stop
```

</td>
</tr>
</table>

### Запуск службы

<table>
<tr><td>systemctl</td><td>service</td></tr>
<tr>
<td>

```bash
systemctl start nginx
```

</td>
<td>

```bash
service nginx start
```

</td>
</tr>
</table>

### Перезапуск службы

<table>
<tr><td>systemctl</td><td>service</td></tr>
<tr>
<td>

```bash
systemctl restart nginx
```

</td>
<td>

```bash
service nginx restart
```

</td>
</tr>
</table>

Перезапуск делает `stop`, потом `start` службы. Если служба отключена, то просто запустит ее.

### Перезагрузка службы

Перезагрузка службы отличается от ее перезапуска. Перезагрузка не отключает службу, а обновляет ее конфигурации на ходу.

Это полезно, например, когда вы изменили конфигурации веб-сервера nginx и нужно будет без отключения обновить ее.

<table>
<tr><td>systemctl</td><td>service</td></tr>
<tr>
<td>

```bash
systemctl reload nginx
```

</td>
<td>

```bash
service nginx reload
```

</td>
</tr>
</table>

### Включение службы

Параметр `enable` в команде `systemctl` делает сервис постоянным, т.е. при перезапуске системы Linux служба автоматически запустится.

```bash
systemctl enable nginx.service
```

Команда, `service` не имеет такой функции. Вместо этого нужно использовать `chkconfig` для управления постоянными службами. Однако, в сервере Linux на stepik такая команда недоступна.

### Отключение службы

Параметр `disable` отменяет постоянство службы, то есть при перезапуске не запустится автоматически. Эта команда не останавливает службу, для этого используйте `stop`.

```bash
systemctl disable nginx.service
```

Команда, `service` не имеет такой функции.

## Команда journalctl для просмотра журнала systemd

```bash
journalctl -u nginx
```

На stepik такая команда не доступна. Используйте на реальных серверах.
