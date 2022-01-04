import pytest

import mlops

def only_mario():
    assert 1==2, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

def test_1():
    assert mlops.somma(1,2) == 3, "something"

def test_2():
    assert mlops.somma(0,0) == 1, '0 + 0 is not 1'