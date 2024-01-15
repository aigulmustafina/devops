def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_nginx_stopped(s):
    cmd = "sudo service nginx status"
    stdout = s.run(cmd)
    assert "nginx is not running" in stdout, "nginx is not stopped: "+ stdout
