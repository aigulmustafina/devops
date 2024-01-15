def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_file_content(s):
    FILEPATH="/home/box/sandbox/jusan"
    FILECONTENT="singularity"
    file_content = s.run("cat -e {}".format(FILEPATH))
    assert file_content == FILECONTENT, "Incorrect file content"
