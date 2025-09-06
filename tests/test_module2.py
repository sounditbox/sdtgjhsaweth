import pytest

from src.module2 import calculate_logarithm


def test_my_fixture(my_fixture):
    assert my_fixture == 42


def test_calculate_logarithm_with_negative_number():
    with pytest.raises(ValueError) as exc_info:
        calculate_logarithm(-1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert (str(exc_info.value)
            == "Логарифм можно вычислить только для положительных чисел")
    print(exc_info)


@pytest.mark.parametrize("x, y, expected",
                         [(1, 2, 3),
                          (4, 5, 9),
                          (7, 8, 15)])
def test_add(x, y, expected):
    assert x + y == expected


