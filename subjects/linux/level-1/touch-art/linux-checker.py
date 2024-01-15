def test_file_types(s):
    files = [
        ("a", "f"),
        ("b", "l"),
        ("c", "f"),
        ("d", "d"),
        ("e", "f"),
        ("f", "f"),
        ("g", "f"),
        ("h", "f"),
    ]
    for name, filetype in files:
        cmd = "find /home/box/touch-art -maxdepth 1 -type {} -name {}".format(filetype, name)
        file_content = s.run(cmd)
        assert file_content.strip() == "/home/box/touch-art/"+name, "Incorrect file type: "+name

def test_file_permissions(s):
    files = [
        ("a", permTextToNum("rwxrwxrwx")),
        ("b", permTextToNum("rwxrwxrwx")),
        ("c", permTextToNum("rw-----wx")),
        ("d", permTextToNum("rw--w--wx")),
        ("e", permTextToNum("rw--w--wx")),
        ("f", permTextToNum("rw-----wx")),
        ("g", permTextToNum("rwx---rwx")),
        ("h", permTextToNum("rwxrwxrwx")),
    ]
    for name, perm in files:
        cmd = "stat -c \"%a\" /home/box/touch-art/"+name
        file_content = s.run(cmd)
        assert file_content.strip() == perm, "Incorrect permission: "+name

def permTextToNum(text):
    res = ""
    for i in range(0, 3):
        cur = 0
        val = text[i*3:i*3+3]
        for i, j in enumerate([4, 2, 1]):
            if val[i] != "-":
                cur += j
        res += str(cur)
    return res
