import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_subtraction():
    assert calculate(5, 2, '-') == 3

def test_calculate_multiplication():
    assert calculate(3, 2, '*') == 6

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_divisionbyzero():
    assert calculate(8, 0, '/') == "Ошибка: Деление на ноль."

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."


