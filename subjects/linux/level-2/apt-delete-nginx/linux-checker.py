def test_nginx_bin(s):
    script = '[ -f "/usr/sbin/nginx" ]'
    cmd = s.run(script)
    assert cmd.succeeded == False, "nginx should be removed!"

def test_nginx_dir(s):
    script = '[ -d "/etc/nginx" ]'
    cmd = s.run(script)
    assert cmd.succeeded == False, "nginx configs should be removed!"
