def check(reply):
    results = [
        "Connection to jusan.kz 80 port [tcp/http] succeeded!",
        "Connection to jusan.kz port 80 [tcp/http] succeeded!"
    ]
    return reply in results
