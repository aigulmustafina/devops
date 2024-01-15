def test_script(s):
    script = "bash /home/box/ps-all.sh"
    solution = "ps -ef"
    postfix = " | grep -v \"ps\" | grep -v \"ps-all.sh\""

    actual_cmd = s.run(script+postfix)
    expected_cmd = s.run(solution+postfix)

    actual = sorted([line.strip() for line in actual_cmd.split("\n")])
    expect = sorted([line.strip() for line in expected_cmd.split("\n")])

    assert actual == expect, "\nexpected:\n{}\n\nactual:\n{}".format("\n".join(expect), "\n".join(actual))
