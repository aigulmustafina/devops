def test_script(s):
    script = "bash /home/box/ps-sort.sh"
    solution = "ps -ef --sort=-pcpu"
    postfix = " | grep -v \"ps\" | grep -v \"ps-sort.sh\""

    actual_cmd = s.run(script+postfix)
    expected_cmd = s.run(solution+postfix)

    actual = sorted([line.strip() for line in actual_cmd.split("\n")])
    expect = sorted([line.strip() for line in expected_cmd.split("\n")])

    assert actual == expect, "\nexpected headers:\n{}\n\nactual headers:\n{}".format("\n".join(expect), "\n".join(actual))
