import pytest

@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print("\nSetup Module2")

@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    print("\nSetup Function2")

@pytest.fixture(scope="class", autouse=True)
def setup_class():
    print("\nSetup Class")

class TestClass:
    def test_it1(self):
        print("Testit1")
        assert True

    def test_it2(self):
        print("Testit2")
        assert True