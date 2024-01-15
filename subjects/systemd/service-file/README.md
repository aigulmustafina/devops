# service-file

Файл конфигурации сервиса имеет расширение `.service`. В нем указывается информация по запуску службы.

Пример конфигурационного файла от сервиса `sshd`, который отвечает за _ssh_ подключения.

```ini
[Unit]
Description=OpenBSD Secure Shell server
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target auditd.service
ConditionPathExists=!/etc/ssh/sshd_not_to_be_run

[Service]
EnvironmentFile=-/etc/default/ssh
ExecStartPre=/usr/sbin/sshd -t
ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
ExecReload=/usr/sbin/sshd -t
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure
RestartPreventExitStatus=255
Type=notify
RuntimeDirectory=sshd
RuntimeDirectoryMode=0755

[Install]
WantedBy=multi-user.target
Alias=sshd.service
```

Описание параметров:

| Название           | Описание                                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------- |
| _Description_      | описание сервиса                                                                             |
| _Documentation_    | список справочных страниц для sshd                                                           |
| _After_            | sshd будет запущен после того, <br>как будут запущены перечисленные сервисы                  |
| _Environment File_ | переменные окружения для sshd                                                                |
| _ExecStart_        | команда для запуска                                                                          |
| _ExecReload_       | команда для перезагрузки                                                                     |
| _WantedBy_         | целевой юнит, к которому относится данный сервис. <br>По дефолту указывают multi-user.target |
