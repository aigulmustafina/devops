def check(token):
    return "ssh-keygen" in token and "ssh-copy-id" in token
