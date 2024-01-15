# ansible-playbook

Задание данного модуля проверяются в конце ментором. Это первая часть проекта. Сделав это задание, переходите к следующему.

### Полезное

- [Модуль apt в Ansible](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)
- [Модуль service в Ansible](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html)

### Задание

1. Для сдачи данного модуля создайте репозиторий в ([ССЫЛКА GITHUB CLASSROOM]). Вести работу будем в нем.
2. Создайте скрипт `setup.sh`, который будет запускать контейнеры для Ansible:
   - запускает образ `atlekbai/local-vps` с именем контейнера `local-vps-22` и перенаправялет порты 22 и 80 внутрь контейнера;
   - устанавливает на сервер ssh-ключ.
3. Проверьте ssh подключение `ssh root@127.0.0.1`, авторизация должна происходить без пароля.
4. Создайте инвентори файл `hosts.ini`, в котором есть группе под названием `lb`. В группе записан наш сервер.
5. Создать плэйбук `playbook.yml`, который:
   - работает с хостами из группы `lb`;
   - содержит таск по установке `nginx` через `apt`;
   - содержит таск по запуску сервиса `nginx` - `started`, `enabled`;
6. Запустите плейбук с указанием инвентори файла.
7. Проверьте, что запрос на сервер работает `curl http://127.0.0.1`
8. Запушьте файлы `setup.sh`, `hosts.ini`, `playbook.yml` в гит.

---

### Ответ

Запуск контейнеров - `setup.sh`

```bash
PORT=22 && docker run -d --rm --name local-vps-$PORT -p $PORT:$PORT -p 80:80 atlekbai/local-vps $PORT

ssh-copy-id root@127.0.0.1 -p 22
```

Инвентари файл - `hosts.ini`

```ini
[lb]
127.0.0.1 ansible_user=root ansible_port=22
```

Плэйбук - `playbook.yaml`

```yaml
---
- hosts: lb
  become: yes

  tasks:
    - name: Установка nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    - name: Запуск nginx
      service:
        name: nginx
        state: started
        enabled: yes
```
