from app import add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(5) is False

