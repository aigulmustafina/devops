# stepik-join-date

Полезные команды:

- Команда для выполнения HTTP запросов `curl`
- Команда для парсинга JSON `jq`

У _stepik.org_ есть публичный API. Через него можно получать общедоступную информацию по платформе.

Например, такой запрос вернет пользователя под id `1`, т.е. самого первого пользователя на _stepik.org_.

```bash
curl -s https://stepik.org:443/api/users/1
```

```
{"meta": {"page": 1, "has_next": false, "has_previous": false}, "users": [{"id": 1, "profile": 1, "is_private": false, "is_active": true, "is_guest": false, "is_organization": false, "short_bio": "", "details": "", "first_name": "Andrey", "last_name": "Balandin", "full_name": "Andrey Balandin", "alias": null, "avatar": "https://stepik.org/users/1/59109f498310fb45ff2ae4642cd06f96fa7382dc/avatar.svg", "cover": null, "city": 498817, "knowledge": 167, "knowledge_rank": 401819, "reputation": 2, "reputation_rank": 111316, "join_date": "2013-07-02T10:41:22Z", "social_profiles": [], "solved_steps_count": 164, "created_courses_count": 0, "created_lessons_count": 2, "issued_certificates_count": 0, "followers_count": 4}]}
```

### Задание

1. В корневой директории `/home/box` создайте файл `stepik.sh`
2. Напишите скрипт в `stepik.sh`, который выведет `join_date` вашего профиля.
3. Дайте права 755 на `stepik.sh`.

Например, для пользователя под id `1` ответ:

```
2013-07-02T10:41:22Z
```

---

### Ответ

```bash
touch /home/box/stepik.sh
chmod 755 /home/box/stepik.sh
cat << EOF > /home/box/stepik.sh
curl -s https://stepik.org:443/api/users/1 | jq --raw-output ".users[0].join_date"
EOF
```
