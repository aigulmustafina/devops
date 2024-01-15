answers = [
    "mr robot",
    "mister robot",
    "мр робот",
    "мистер робот",
]

replace_elems = [".", ",", "!"]

def check(reply):
    reply = reply.lower()
    for elem in replace_elems:
        reply = reply.replace(elem, "")
    return reply in answers
