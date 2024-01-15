import re

pattern=r"[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}T[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}Z"

def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_file_permissions(s):
    cmd = "stat -c \"%a\" /home/box/stepik.sh"
    file_content = s.run(cmd)
    assert file_content.strip() == "755", "Incorrect file permissions"

def test_stepik_sh(s):
    cmd = "/home/box/stepik.sh"
    file_content = s.run(cmd)
    matches = re.search(pattern, file_content)
    assert matches is not None, "Incorrect output: "+file_content
