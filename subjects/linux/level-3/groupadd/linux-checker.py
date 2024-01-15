def test_user(s):
    login = "john"
    expected = "john"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "no user "+login

def test_user_name(s):
    login = "john"
    expected = "John Cena"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f5".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "name doesn't match"

def test_user_password(s):
    login = "john"
    password = "myTimeIsNoW!"
    passhash_script = "mkpasswd -m sha-512 \'{}\' $(sudo cat /etc/shadow | grep {} | cut -d ':' -f2 - | cut -d '$' -f3 -)".format(password, login)
    hashedpass_script = "sudo cat /etc/shadow | grep {} | cut -d ':' -f2 -".format(login)
    passhash_cmd = s.run(passhash_script)
    hashedpass_cmd = s.run(hashedpass_script)
    assert passhash_cmd == hashedpass_cmd, "incorrect password"

def test_user_groups(s):
    login = "john"
    target_groups = [
        "kings",
        "john",
    ]
    for target_group in target_groups:
        script = "cat /etc/group | grep \'^{}:\'".format(target_group)
        cmd = s.run(script)
        assert login in cmd, "not in group "+target_group

def test_user_file(s):
    expected = [
        "john /home/john/config-john.txt",
        "kings /home/john/config-kings.txt",
    ]
    filepath = [
        "/home/john/config-john.txt",
        "/home/john/config-kings.txt",
    ]
    for i, fp in enumerate(filepath):
        exp = expected[i]
        script = "ls -l "+fp+" | awk '{ print $4, $9 }'"
        cmd = s.run(script)
        assert cmd.strip() == exp, fp+": failed"

def test_file_content(s):
    paths=[
        "/home/john/config-john.txt",
        "/home/john/config-kings.txt",
    ]
    FILECONTENT="success: true"

    for fp in paths:
        script = "cat {}".format(fp)
        file_content = s.run(script)
        assert file_content.strip() == FILECONTENT, "incorrect file content:"+fp
