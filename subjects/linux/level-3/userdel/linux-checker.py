def test_user(s):
    login = "john"
    script = 'cat /etc/passwd | grep {}'.format(login)
    cmd = s.run(script)
    assert cmd.succeeded == False, "user not deleted"

def test_user_home(s):
    login = "john"
    script = '[ -d "/home/{}" ]'.format(login)
    cmd = s.run(script)
    assert cmd.succeeded == False, "home directory is not removed"
