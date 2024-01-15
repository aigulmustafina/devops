def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_user(s):
    login = "mark"
    expected = "mark"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "no user "+login

def test_user_name(s):
    login = "mark"
    expected = "Mark Twain"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f5".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "name doesn't match"

def test_user_shell(s):
    login = "mark"
    expected = "/bin/bash"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f7".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "shell doesn't match"

def test_user_group(s):
    login = "mark"
    expected = "mark"
    script = "cat /etc/group | grep '{}:' | cut -d ':' -f1".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "group doesn't match"

def test_user_group_bin(s):
    login = "mark"
    target_group = "bin"
    script = "cat /etc/group | grep \'^{}:\'".format(target_group)
    cmd = s.run(script)
    assert login in cmd, "not in group "+target_group

def test_user_group_staff(s):
    login = "mark"
    target_group = "staff"
    script = "cat /etc/group | grep \'^{}:\'".format(target_group)
    cmd = s.run(script)
    assert login in cmd, "not in group "+target_group

def test_user_uid(s):
    login = "mark"
    expected = "567"
    script = "cat /etc/passwd | grep {} | cut -d ':' -f3".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "uid doesn't match"

def test_user_expiration(s):
    login = "mark"
    expected = "Nov 30, 2035"
    script = "sudo chage -l {} | grep \"Account expires\" | cut -d ':' -f2".format(login)
    cmd = s.run(script)
    assert cmd.strip() == expected, "expiration: fail"

def test_user_home(s):
    script = '[ -d "/home/marktwain" ]'
    cmd = s.run(script)
    assert cmd.succeeded == True, "no home directory"

def test_user_skel(s):
    script = '[ -d "/home/marktwain/fs" ]'
    cmd = s.run(script)
    assert cmd.succeeded == True, "skeleton directory: fail"

def test_user_file(s):
    expected = "mark /home/marktwain/config.txt"
    filepath = "/home/marktwain/config.txt"

    script = "ls -l "+filepath+" | awk '{ print $3, $9 }'"
    cmd = s.run(script)
    assert cmd.strip() == expected, "config.txt: failed"

def test_file_content(s):
    FILEPATH="/home/marktwain/config.txt"
    FILECONTENT="success: true"

    script = "cat {}".format(FILEPATH)
    file_content = s.run(script)
    assert file_content.strip() == FILECONTENT, "incorrect file content"

def test_user_password(s):
    login = "mark"
    password = "S@wYer"
    passhash_script = "mkpasswd -m sha-512 \'{}\' $(sudo cat /etc/shadow | grep {} | cut -d ':' -f2 - | cut -d '$' -f3 -)".format(password, login)
    hashedpass_script = "sudo cat /etc/shadow | grep {} | cut -d ':' -f2 -".format(login)
    passhash_cmd = s.run(passhash_script)
    hashedpass_cmd = s.run(hashedpass_script)
    assert passhash_cmd == hashedpass_cmd, "incorrect password"
