def check(reply):
    answers = [
        "kill -15 999",
        "kill -SIGTERM 999",
        "kill 999",
    ]
    for answer in answers:
        if answer in reply:
            return True
    return False
