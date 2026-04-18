import pytest
from your_module import catalan

def test_catalan():
    assert catalan(0) == 1
    assert catalan(1) == 1
    assert catalan(2) == 2
    assert catalan(3) == 5
    assert catalan(4) == 14
    assert catalan(5) == 42

def test_catalan_invalid_input():
    with pytest.raises(ValueError):
        catalan(-1)
    with pytest.raises(ValueError):
        catalan(1.5)

def test_catalan_large_input():
    assert catalan(10) == 16796
