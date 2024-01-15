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

class DirStruct:
    @staticmethod
    def get_level(line: str):
        return (len(line) - len(line.lstrip()))/4

    @staticmethod
    def create_structure_helper(lines: list, idx: int, level: int, parent: str):
        for i in range(idx, len(lines)):
            line = lines[i]
            if not line:
                continue
            if DirStruct.get_level(line) == level:
                name = line.strip()
                if name.endswith("/:") or name.endswith("/"):
                    name = name.replace(":", "")
                    os.system("mkdir -p {}".format(parent+name))
                    DirStruct.create_structure_helper(lines, i, level+1, parent+name)
                else:
                    os.system("touch {}".format(parent+name))
            if i+1 < len(lines) and DirStruct.get_level(lines[i+1]) < level:
                break

    @staticmethod
    def create_structure(text: str):
        if not text:
            return
        text = text.strip()
        DirStruct.create_structure_helper(text.split("\n"), 0, 0, "./")

def init():
    DIRECTORY_STRUCTURE = """
Documents/:
    hello.txt
    review.html
    passport/:
        front-side.jpg
        back-side.jpg
Downloads/:
    billie-jean.mp3
    lose-yourself.mp3
    """
    DirStruct.create_structure(DIRECTORY_STRUCTURE)

SCRIPT_BODY = """
::code
# write your code here

::footer
"""

SOLUTION_CMD = "ls -tF1"


def test_output():
    user_script = UserScript()
    actual_output = user_script.run(SCRIPT_BODY)
    expected_output = execute(SOLUTION_CMD)

    actual = sorted([line.strip() for line in actual_output.split("\n")])
    expect = sorted([line.strip() for line in expected_output.split("\n")])

    if actual == expect:
        print("SUCCESS")
    else:
        print("FAIL")
        print("actual:\n{}".format("\n".join(actual)))
        print("\n")
        print("expected:\n{}".format("\n".join(expect)))

init()
test_output()
