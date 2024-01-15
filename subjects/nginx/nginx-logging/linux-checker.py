def test_output(s):
    exp = "<h1>Welcome to nginx!</h1>"
    cmd = 'curl localhost'
    stdout = s.run(cmd)
    assert exp in stdout, "wrong output:"+stdout
