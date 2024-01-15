def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_file_content(s):
    FILEPATH="/home/box/second"
    FILECONTENT="touch"
    file_content = s.run("cat {}".format(FILEPATH))
    assert file_content.strip() == FILECONTENT, "Incorrect file content"

def test_file_permissions(s):
    cmd = "stat -c \"%a\" /home/box/second"
    file_content = s.run(cmd)
    assert file_content.strip() == "632", "Incorrect file permissions"
