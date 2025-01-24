import pytest

from homework_3.task_5_built_in import *


def test_custom_length_function_positive():
    assert custom_len([1, 2, 3]) == 3, "Custom length function should return 3 integers"


def test_custom_length_function_empty():
    assert custom_len([]) == 0, "Custom length function should return an empty list"


def test_custom_length_function_negative():
    assert custom_len([1]) != 0, "The length function should return 1 but return 0 instead"


def test_custom_sum_with_no_arguments():
    with pytest.raises(ValueError):
        assert custom_sum(), "ValueError Exception should be raised"


def test_custom_sum_with_one_iterable_argument():
    assert custom_sum([1, 2, 3]) == 6, "The sum function should return 6"


def test_custom_sum_with_one_non_iterable_argument():
    with pytest.raises(TypeError):
        custom_sum(5)


def test_custom_sum_with_one_string_argument():
    with pytest.raises(TypeError):
        custom_sum("v")


def test_custom_sum_with_multiple_arguments():
    assert custom_sum(1, 2, 3) == 6, "The sum function should return 6"


def test_custom_min_with_no_arguments():
    with pytest.raises(ValueError):
        assert custom_min(), "ValueError Exception should be raised"


def test_custom_min_with_one_iterable_argument():
    assert custom_min([1, 2, 3]) == 1, "The min function should return 1"


def test_custom_min_with_one_non_iterable_argument():
    with pytest.raises(TypeError):
        custom_min(5)


def test_custom_min_with_one_string_argument():
    with pytest.raises(TypeError):
        custom_min("v")


def test_custom_min_with_two_arguments():
    assert custom_min(1, 2) == 1, "The min function should return 1"
