# nginx-status

Чтобы узнать, работает ли сервис, запустите команду:

<table>
<tr><td>systemctl</td><td>service</td></tr>
<tr>
<td>

```bash
sudo systemctl status sshd
```

</td>
<td>

```bash
sudo service sshd status
```

</td>
</tr>
</table>

```
● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2021-10-01 11:12:50 UTC; 5 months 11 days ago
     Docs: man:sshd(8)
           man:sshd_config(5)
 Main PID: 88592 (sshd)
    Tasks: 3 (limit: 7003)
   Memory: 21.4M
   CGroup: /system.slice/ssh.service
           ├─ 88592 /usr/sbin/sshd -D
           ├─108984 sshd: root [priv]
           └─108986 sshd: root [net]

Mar 14 08:13:25 app-02 sshd[108922]: Failed password for root from 103.50.205.142 port 42754 ssh2
Mar 14 08:13:25 app-02 sshd[108987]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=20.203.189.122  user=root
```

Поле `Active` имеет значение `active (running)` - это значит, что сервис работает. Также, указано много другой полезной информации, а снизу последние логи службы.

### Задание

1. Перечислите все названия полей в `systemctl status` через запятую

---

### Ответ

```
Loaded, Active, Docs, Main PID, Tasks, Memory, CGroup
```
