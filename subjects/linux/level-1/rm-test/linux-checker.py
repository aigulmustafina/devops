def test_connection(s):
    assert s.run('true').succeeded, "Could not connect to server"

def test_directory(s):
    expected_output = """
helper_helper.py                                                                           
helper_init.py                                                                             
helper.py                                                                                  
__init___helper.py                                                                         
__init___init.py                                                                           
__init__.py                                                                                
main_helper.py                                                                             
main_init.py                                                                               
main.py                                                                                    
project_helper.py                                                                          
project_init.py                                                                            
project.py                                                                                 
util_helper.py                                                                             
util_init.py                                                                               
util.py
"""
    cmd = "ls -F1 /home/box/project"
    actual_output = s.run(cmd)

    actual = sorted(actual_output.strip().split())
    expected = sorted(expected_output.strip().split())
    
    error_msg = "actual:\n{}\n\nexpected:\n{}".format("\n".join(actual), "\n".join(expected))

    assert len(actual) == len(expected), error_msg
    for i in range(len(expected)):
        assert actual[i].strip() == expected[i].strip(), error_msg
