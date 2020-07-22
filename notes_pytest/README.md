## Xunit style setup and teardown

### Test class and test methods in classes

```bash
===> pytest -vs test_xunit_class.py 
===================================================== test session starts ======================================================
platform linux -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /home/a1t20v21/.pyenv/tddpython/bin/python3
cachedir: .pytest_cache
rootdir: /home/a1t20v21/workspace/tdd_python/summary_pytest
collected 2 items                                                                                                              

test_xunit_class.py::TestClass::test1 
setup class

Setup Method test1
Test1
PASSED
Tearing down test1

test_xunit_class.py::TestClass::test2 
Setup Method test2
Test2
PASSED
Tearing down test2

Tearing Down class


====================================================== 2 passed in 0.02s =======================================================

```
