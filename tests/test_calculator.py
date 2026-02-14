import pytest
from src.calculator import add, subtract

class CalculatorTestCase:
    def test_add(self):
        assert add(2, 5) == 7
        assert add(0, 4) == 4
        assert add(2, 2) == 4
        assert add(3, 7) == 10

    def test_subtract(self):
        assert subtract(4, 2) == 2
        assert subtract(5, 1) == 4
        assert subtract(4, 0) == 4
        assert subtract(0, 3) == -3
