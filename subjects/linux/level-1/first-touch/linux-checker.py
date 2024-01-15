def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_file_content(s):
    FILEPATH="/home/box/jusan"
    FILECONTENT="singularity"
    file_content = s.run("cat {}".format(FILEPATH))
    assert file_content.strip() == FILECONTENT, "Incorrect file content"
