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

SCRIPT_BODY = """
::code
# write your code here

::footer
"""


def test_output():
    user_script = UserScript()
    user_script.run(SCRIPT_BODY)
    actual_output = execute("cat ./output.txt")
    expected_output = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec neque purus,
rutrum vel purus eget, mattis aliquam tortor. Morbi rhoncus metus faucibus
tortor blandit, in luctus leo ultrices. Donec finibus vulputate ex, vel
feugiat erat. Ut ultrices felis sit amet urna tincidunt tempor. Suspendisse
vel eleifend augue. Nam porta leo urna. Mauris augue mi, lacinia in consectetur
a, accumsan nec nibh. Mauris ornare pulvinar lorem, sit amet venenatis enim
feugiat non. Praesent aliquet nec lorem ac interdum. Mauris quis finibus orci,
at tempor mi.
    """

    actual = [line.strip() for line in actual_output.strip().split("\n")]
    expect = [line.strip() for line in expected_output.strip().split("\n")]

    if actual == expect:
        print("SUCCESS")
    else:
        print("FAIL")
        print("actual:\n{}".format("\n".join(actual)))
        print("\n")
        print("expected:\n{}".format("\n".join(expect)))

test_output()
