import pytest

from src.module import f


def test_f():
    assert f(2) == 4
    assert f(-2) == 4
    assert f(0) == 0
    assert f(1) == 1
    with pytest.raises(TypeError):
        f("a")


def test_f2():
    assert f(2) == 4
    assert f(-2) == 4
    assert f(0) == 0
    assert f(1) == 1
    with pytest.raises(TypeError):
        f("a")