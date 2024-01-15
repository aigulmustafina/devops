def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_directory(s):
    expected_output = """
/home/box/project/                                                              
/home/box/project/pkg                                                           
/home/box/project/pkg/util                                                      
/home/box/project/pkg/util/helper.go                                            
/home/box/project/pkg/util/util.go                                              
/home/box/project/pkg/util/util_test.go                                         
/home/box/project/README.md                                                     
/home/box/project/usecase                                                       
/home/box/project/usecase/registration                                          
/home/box/project/usecase/registration/registration.go                          
/home/box/project/usecase/registration/registration_test.go
    """
    cmd = "find /home/box/project/ | sort"
    actual_output = s.run(cmd)

    actual = sorted(actual_output.strip().split())
    expected = sorted(expected_output.strip().split())

    error_msg = "actual:\n{}\n\nexpected:\n{}".format("\n".join(actual), "\n".join(expected))
    
    assert len(actual) == len(expected), error_msg
    for i in range(len(expected)):
        assert actual[i].strip() == expected[i].strip(), error_msg
