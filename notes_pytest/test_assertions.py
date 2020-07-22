from pytest import approx

def test_int_assert():
    assert 1 == 1

def test_str_assert():
    assert "Hello" == "Hello"

def test_float_assert():
    assert 3.0 == 3.0

def test_array_assert():
    assert [1, 2, 3] == [1, 2, 3]

def test_dict_assert():
    assert {"1":1} == {"1":1}

def test_float_op():
    # The below == assertion will fail (commented)
    # assert (0.1 + 0.2) == 0.3
    assert (0.1 + 0.2) == approx(0.3)