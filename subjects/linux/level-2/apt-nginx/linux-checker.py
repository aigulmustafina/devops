def test_apt_update(s):
    cmd = "sudo apt update"
    stdout = s.run(cmd)
    assert "All packages are up to date." in stdout, "System not updated!"

def test_apt_upgrade(s):
    cmd = "sudo apt upgrade"
    stdout = s.run(cmd)
    assert "0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded." in stdout, "System not upgraded!"

def test_apt_nginx(s):
    cmd = "sudo nginx -v"
    stdout = s.run(cmd)
    assert stdout.succeeded, "nginx not installed"
