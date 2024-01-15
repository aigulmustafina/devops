::python3.10
::header
import os

def execute(cmd):
    stream = os.popen(cmd)
    output = stream.read()
    return output

class UserScript:
    SCRIPT_NAME = "user_script.sh"

    def run(self, script_body) -> str:
        with open(self.SCRIPT_NAME, "w") as file:
            file.write(script_body)
        output = execute("bash "+self.SCRIPT_NAME)
        return output

def init():
    accessBody = """
93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
217.168.17.5 - - [17/May/2015:08:05:34 +0000] "GET /downloads/product_1 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
217.168.17.5 - - [17/May/2015:08:05:09 +0000] "GET /downloads/product_2 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
93.180.71.3 - - [17/May/2015:08:05:57 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
217.168.17.5 - - [17/May/2015:08:05:02 +0000] "GET /downloads/product_2 HTTP/1.1" 404 337 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
217.168.17.5 - - [17/May/2015:08:05:42 +0000] "GET /downloads/product_1 HTTP/1.1" 404 332 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
80.91.33.133 - - [17/May/2015:08:05:01 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
93.180.71.3 - - [17/May/2015:08:05:27 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"
    """
    accessFilePath = "./access.log"
    with open(accessFilePath, "w") as file:
            file.write(accessBody.strip())

SCRIPT_BODY = """
::code
# write your code here

::footer
"""

SOLUTION_CMD = "head -n 5 ./access.log"


def test_output():
    user_script = UserScript()
    actual_output = user_script.run(SCRIPT_BODY)
    expected_output = execute(SOLUTION_CMD)

    actual = [line.strip() for line in actual_output.strip().split("\n")]
    expect = [line.strip() for line in expected_output.strip().split("\n")]

    if actual == expect:
        print("SUCCESS")
    else:
        print("FAIL")
        print("actual:\n{}".format("\n".join(actual)))
        print("\n")
        print("expected:\n{}".format("\n".join(expect)))

init()
test_output()
