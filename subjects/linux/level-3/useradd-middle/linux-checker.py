def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_user(s):
    login = "murat"
    expected = "murat"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "no user "+login

def test_user_name(s):
    login = "murat"
    expected = "Murat Serik"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f5".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "name doesn't match"

def test_user_shell(s):
    login = "murat"
    expected = "/bin/sh"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f7".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "name doesn't match"

def test_user_group(s):
    login = "murat"
    expected = "2"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f4".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "group doesn't match"

def test_user_home(s):
    login = "murat"
    script = '[ -d "/home/{}" ]'.format(login)
    cmd = s.run(script)
    assert cmd.succeeded == True, "no home directory"

def test_user_file(s):
    expected = "murat /home/murat/config.txt"
    filepath = "/home/murat/config.txt"

    script = "ls -l "+filepath+" | awk '{ print $3, $9 }'"
    cmd = s.run(script)
    assert cmd.strip() == expected, "config.txt: failed"

def test_file_content(s):
    FILEPATH="/home/murat/config.txt"
    FILECONTENT="success: true"

    script = "cat {}".format(FILEPATH)
    file_content = s.run(script)
    assert file_content.strip() == FILECONTENT, "incorrect file content"

def test_user_password(s):
    login = "murat"
    password = "H3l70!vv0r7d"
    passhash_script = "mkpasswd -m sha-512 \'{}\' $(sudo cat /etc/shadow | grep {} | cut -d ':' -f2 - | cut -d '$' -f3 -)".format(password, login)
    hashedpass_script = "sudo cat /etc/shadow | grep {} | cut -d ':' -f2 -".format(login)
    passhash_cmd = s.run(passhash_script)
    hashedpass_cmd = s.run(hashedpass_script)
    assert passhash_cmd == hashedpass_cmd, "incorrect password"
