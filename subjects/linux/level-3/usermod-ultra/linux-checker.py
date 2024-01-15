def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_user(s):
    login = "serikbek"
    expected = "serikbek"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "no user "+login

def test_user_name(s):
    login = "serikbek"
    expected = "Serik"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f5".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "name doesn't match"

def test_user_blocked(s):
    login = "serikbek"
    expected = "!"
    script = "sudo cat /etc/shadow | grep {} | cut -d ':' -f2".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "user is not blocked"

def test_user_groups(s):
    login = "serikbek"
    target_groups = [
        "daemon",
        "bin",
        "mail",
    ]
    for target_group in target_groups:
        script = "cat /etc/group | grep \'^{}:\'".format(target_group)
        cmd = s.run(script)
        assert login in cmd, "not in group "+target_group
