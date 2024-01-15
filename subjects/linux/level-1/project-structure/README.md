# project-structure

### Задание

1. В корневой директории `/home/box` создайте папку `project` в корневой директории. В ней создайте такую структуру файлов и папок как показано ниже:

```
.
├── README.md
├── usecase
│   └── registration
│       ├── registration.go
│       └── registration_test.go
└── pkg
    └── util
        ├── helper.go
        ├── util_test.go
        └── util.go

```

---

### Ответ

```bash
mkdir project
cd project
touch README.md
mkdir -p ./usecase/registration
touch ./usecase/registration/registration{,\_test}.go
mkdir -p ./pkg/util
touch ./pkg/util/{helper.go,util_test.go,util.go}
```
