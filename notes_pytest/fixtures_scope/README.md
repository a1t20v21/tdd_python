```bash
===> pytest -v -s 
=================================================== test session starts ====================================================
platform linux -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /home/a1t20v21/.pyenv/tddpython/bin/python3
cachedir: .pytest_cache
rootdir: /home/a1t20v21/workspace/tdd_python/notes_pytest/fixtures_scope
collected 4 items                                                                                                          

test_file1.py::test1 
Setup - Session

Setup - Module1

Setup - Function1

Executing test1
PASSED
test_file1.py::test2 
Setup - Function1

Executing test2
PASSED
test_file2.py::TestClass::test_it1 
Setup Module2

Setup Class

Setup Function2
Testit1
PASSED
test_file2.py::TestClass::test_it2 
Setup Function2
Testit2
PASSED

==================================================== 4 passed in 0.01s =====================================================

```