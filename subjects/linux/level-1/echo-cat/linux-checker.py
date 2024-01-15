def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_file_presence(s):
    FILEPATH="/home/box/sandbox/hello-jusan"
    file_content = s.run("ls {}".format(FILEPATH))
    assert file_content.strip() == FILEPATH, "Incorrect file"
