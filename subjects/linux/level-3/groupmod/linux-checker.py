def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_group(s):
    script = "cat /etc/group | grep '^kingdom:'"
    cmd = s.run(script)
    assert cmd.succeeded, "no group kingdom "
