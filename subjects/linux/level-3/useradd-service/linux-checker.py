def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_user(s):
    login = "ghost"
    expected = "ghost"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "no user "+login

def test_user_name(s):
    login = "ghost"
    expected = "Ghost Background Service"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f5".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "name doesn't match"

def test_user_shell(s):
    login = "ghost"
    expected = "/usr/sbin/nologin"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f7".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "shell doesn't match"

def test_user_group(s):
    login = "ghost"
    expected = "ghost"
    script = "cat /etc/group | grep '{}:' | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "group doesn't match"

def test_user_system(s):
    login = "ghost"
    expected = 1000
    script = "cat /etc/passwd | grep {} | cut -d ':' -f3".format(login)
    cmd = s.run(script)
    assert int(cmd.strip()) < expected, "not a system user"

def test_user_home(s):
    login = "ghost"
    script = "[ -d \"$(cat /etc/passwd | grep \'{}\' | cut -d \':\' -f6 -)\" ]".format(login)
    cmd = s.run(script)
    assert cmd.succeeded == False, "home directory present"
