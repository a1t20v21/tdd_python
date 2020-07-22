import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("\nSetup - Session")

@pytest.fixture(scope="module", autouse=True)
def setup_module1():
    print("\nSetup - Module1")

@pytest.fixture(scope="function", autouse=True)
def setup_function1():
    print("\nSetup - Function1")

def test1():
    print("\nExecuting test1")
    assert True

def test2():
    print("\nExecuting test2")
    assert True