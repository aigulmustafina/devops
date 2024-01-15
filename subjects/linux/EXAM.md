## 1. Level-1: Жить в Linux
  
### 1. Как создать и удалить каталог в Linux?
  - [x] mkdir dir_name && rmdir dir_name
  - [ ] cat dir_name && rmdir dir_name
  - [ ] ls dir_name && mkdir dir_name
  - [ ] cp dir_name && mv dir_name

### 2. Как создать файл и вывести в консоль его содержимое в Linux?
  - [ ] touch filename && mv filename
  - [x] touch filename && cat filename
  - [ ] create filename && show filename
  - [ ] run filename && cat filename

### 3. Выберите правильную команду для поиска всех файлов с расширением .pdf в текущем каталоге
  - [ ] find .-name "*pfd"
  - [ ] find "pdf" -name "*"
  - [ ] find "*.pdf" -name .
  - [x] find . -name "*.pdf"

### 4. Создайте файл file и задайте ему права доступа -rwxrwxrwx
  - [x] touch file && chmod 777 file
  - [ ] touch file && chmod 770 file
  - [ ] create file && chmod 660 file
  - [ ] touch file & chmod 677 file

### 5. Удалите сначала все .txt файлы, а потом все содержимое папки и саму папку
  - [ ] rm -rf
  - [ ] rm *.txt && rm -all
  - [x] rm *.txt && rm -rf *
  - [ ] rm *.txt && rm .

### 6. Выведите в консоль последние 10 строк файла access.log
  - [ ] tar access.log
  - [ ] ls access.log
  - [ ] cd access.log
  - [x] tail -n 10 ./access.log

### 7. Выберите комбинацию команд, которая покажет в файле ./access.log только линии, содержащие ERROR 404
  - [ ] tar access.log
  - [ ] ls access.log
  - [x] cat ./access.log | grep "ERROR 404"
  - [ ] tail -n 5 ./access.log

### 8. Выберите команду, которая заменит в файле `access.log` текст `ERROR 404` на `FAIL` глобально
  - [x] cat ./access.log | sed "s/ERROR 404/FAIL/g" > ./access.log
  - [ ] cat ./access.log | sed "ERROR\404 -> FAIL" > ./access.log
  - [ ] cat ./access.log | sed "ERROR\404|FAIL" > ./access.log
  - [ ] cat ./access.log | sed "ERROR\404>FAIL" > ./access.log

## 2. Level-2: Настройка сервера

### 9. Выберите команду для установки пакета `vim`
  - [ ] sudo apt add vim
  - [ ] sudo apt activate vim
  - [ ] sudo apt setup vim
  - [x] sudo apt install -y vim

### 10. Выберите команду для полного удаления пакета `vim`
  - [ ] sudo apt escape vim
  - [x] sudo apt purge vim
  - [ ] sudo apt destroy vim
  - [ ] sudo apt install --remove vim

## 3. Level-3: Пользователи и группы

### 11. Создайте учетную запись с именем пользователя test и полным именем Test Test.
  - [ ] sudo add_user -c test "Test Test"
  - [ ] sudo useradd -c test "Test Test"
  - [ ] sudo newuser -c "Test Test" test
  - [x] sudo useradd -c "Test Test" test

### 12. Создайте учетную запись с именем пользователя test и полным именем Test Test. Установите оболочку по умолчанию (англ. "default shell", см. флаг -s) - /bin/sh.
  - [x] sudo useradd -c "Test Test" -s "/bin/sh" -m -g "bin" test
  - [ ] sudo add_user -c "Test Test" -s "/bin/sh" -m -g "bin" test
  - [ ] sudo useradd -c test "Test Test" -s "/bin/sh" -m -g "bin"
  - [ ] sudo useradd -c "Test Test" "/bin/sh" "bin" test

### 13. Измените учетную запись с именем пользователя test на логин - mark.
  - [ ] sudo userchange -l "mark" test
  - [ ] sudo usermod test -l mark
  - [x] sudo usermod -l "mark" test
  - [ ] sudo usermod mark test

### 14. Создайте новую группу `rulers`.
  - [x] sudo groupadd rulers
  - [ ] sudo add_group rulers
  - [ ] sudo newgroup rulers
  - [ ] sudo creategroup rulers

## 4. Level-4: Процессы

### 15. Перечислите все запущенные процессы с полным набором столбцов информации в отсортированном по использовании CPU порядке (прим. "cpu utilization") по убыванию.
  - [ ] list -ef --sort=-pcpu
  - [ ] ps -ef --sort=-processor
  - [x] ps -ef --sort=-pcpu
  - [ ] ps --sort=-processor

### 16. Прислать команду завершения процесса c PID 555 сигналом SIGKILL.
  - [x] kill -SIGKILL 555
  - [ ] sigkill 555
  - [ ] killprocess 555
  - [ ] SIGKILL 555

## 5. Level-5: Сети

### 17. Что означает интерфейс `eth0`?
  - [ ] Виртуальный интерфейс, присутствующий по умолчанию в любом Linux.
  - [x] Интерфейс, связанный с сетевой картой, работающей через Ethernet (по кабелю).
  - [ ] Интерфейс, связанный с сетевой картой, работающей через Wi-Fi.
  - [ ] Интерфейс, связанный с сетевой картой, работающей через сотовую связь.

### 18. Что означает интерфейс `lo`?
  - [ ] Интерфейс, работающий через сотовую связь.
  - [ ] Интерфейс, присутствующий по умолчанию в любом Linux, связанный с сетевой картой.
  - [ ] Интерфейс, связанный с сетевой картой, работающей через Wi-Fi.
  - [x] Виртуальный интерфейс, присутствующий по умолчанию в любом Linux.

### 19. Какая команда используется для проверки подключения?
  - [x] nc
  - [ ] tcp
  - [ ] cn
  - [ ] conn

### 20. Какой сервис (PID и название сервиса) запущено на 25 порту?
```
$ sudo netstat -tupln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      88592/sshd
tcp        0      0 0.0.0.0:8088            0.0.0.0:*               LISTEN      68131/python
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      121934/postgres
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      1262/master
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      113832/nginx: worke
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      113832/nginx: worke
```
  - [ ] 88592/sshd
  - [ ] 68131/python
  - [ ] 113832/nginx: worke
  - [x] 1262/master
