import re

UNIT = {
    "Description":["Jusan Management server"],
    "After":["sshd.service nginx.service"],
    "ConditionPathExists":["/opt/jusan/server"],
}

SERVICE = {
    "ExecStart":["/opt/jusan/server 8080"],
    "ExecReload":["/bin/kill -HUP $MAINPID", "/opt/jusan/server -t"],
}

INSTALL = {
    "WantedBy":["multi-user.target"],
    "Alias":["jusand.service"],
}

def to_dict(str):
    if len(str) == 0:
        return {}
    res = {}
    for line in str.split("\n"):
        key, value = line.split("=", 1)
        if key.strip() not in res:
            res[key.strip()] = [value.strip()]
        else:
            res[key.strip()].append(value.strip())
            res[key.strip()] = sorted(res[key.strip()])
    return res

def check(reply):
    if not reply:
        return False
    reply = reply.strip()
    tokens = re.compile("\[\w+\]").split(reply)
    if tokens:
        tokens = tokens[1:]
    tokens = [to_dict(token.strip()) for token in tokens]
    unit, service, install = tokens

    if not unit == UNIT:
        return False, "error in [Unit] section"
    if not service == SERVICE:
        return False, "error in [Service] section"
    if not install == INSTALL:
        return False, "error in [Install] section"
    return True
