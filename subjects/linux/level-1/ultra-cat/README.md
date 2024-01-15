# ultra-cat

### Полезное

- `cat EOF`

### Задание

1. Написать скрипт, который запишет в файл `output.txt` следующие линии:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec neque purus,
rutrum vel purus eget, mattis aliquam tortor. Morbi rhoncus metus faucibus
tortor blandit, in luctus leo ultrices. Donec finibus vulputate ex, vel
feugiat erat. Ut ultrices felis sit amet urna tincidunt tempor. Suspendisse
vel eleifend augue. Nam porta leo urna. Mauris augue mi, lacinia in consectetur
a, accumsan nec nibh. Mauris ornare pulvinar lorem, sit amet venenatis enim
feugiat non. Praesent aliquet nec lorem ac interdum. Mauris quis finibus orci,
at tempor mi.
```

---

### Ответ

```
cat << EOF > output.txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec neque purus,
rutrum vel purus eget, mattis aliquam tortor. Morbi rhoncus metus faucibus
tortor blandit, in luctus leo ultrices. Donec finibus vulputate ex, vel
feugiat erat. Ut ultrices felis sit amet urna tincidunt tempor. Suspendisse
vel eleifend augue. Nam porta leo urna. Mauris augue mi, lacinia in consectetur
a, accumsan nec nibh. Mauris ornare pulvinar lorem, sit amet venenatis enim
feugiat non. Praesent aliquet nec lorem ac interdum. Mauris quis finibus orci,
at tempor mi.
EOF
```
