import pytest

@pytest.fixture(params=[1, 2, 3], autouse=True)
def setup_data(request):
    print("\nSetup Data")
    return request.param

def test1():
    print(setup_data)