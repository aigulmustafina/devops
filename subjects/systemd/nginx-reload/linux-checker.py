def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_server(s):
    cmd = "curl localhost:9090"
    stdout = s.run(cmd)
    expected = "hello, from jusan-devops course!"
    assert expected in stdout, "server not added: "+ stdout
