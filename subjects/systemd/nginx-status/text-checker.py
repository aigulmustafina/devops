def check(reply):
    fields = [
        "Loaded",
        "Active",
        "Docs",
        "Main PID",
        "Tasks",
        "Memory",
        "CGroup"
    ]
    reply = reply.lower()
    for field in fields:
        if not field.lower() in reply:
            return False
    return True
