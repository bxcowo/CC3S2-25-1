import pytest

from src.belly import Belly

def test_add_int_cucumber():
    belly = Belly()
    belly.comer(23)
    assert belly.pepinos_comidos == 23

def test_add_float_cucumber():
    belly = Belly()
    belly.comer(12.25)
    assert belly.pepinos_comidos == 12.25

def test_add_negative_cucumber():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(-123)
