def test_script(s):
    script = "bash /home/box/ps-column.sh"
    solution = "ps -eo pid,user,group,vsize,pcpu,cmd --sort=-pcpu"
    postfix = " | grep -v \"ps\" | grep -v \"ps-column.sh\""

    actual_cmd = s.run(script+postfix)
    expected_cmd = s.run(solution+postfix)

    actual_list = [line.strip() for line in actual_cmd.split("\n")][1:]
    expect_list = [line.strip() for line in expected_cmd.split("\n")][1:]

    actual = sorted(actual_list)
    expect = sorted(expect_list)

    assert actual == expect, "\nexpected:\n{}\n\nactual:\n{}".format("\n".join(expect), "\n".join(actual))
