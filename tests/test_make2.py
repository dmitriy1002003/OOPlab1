import os
import sys
import pytest

# подключение src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from task_package_2.zad_2 import Fraction


class TestFraction:

    def test_initialization(self):
        f = Fraction(3, 4)
        assert f.num == 3
        assert f.den == 4

    def test_zero_denominator(self):
        with pytest.raises(ValueError):
            Fraction(1, 0)

    def test_reduce(self):
        f = Fraction(6, 8)
        assert f.num == 3
        assert f.den == 4

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        assert result.num == 5
        assert result.den == 6

    def test_sub(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        result = f1 - f2
        assert result.num == 1
        assert result.den == 2

    def test_mul(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 5)
        result = f1 * f2
        assert result.num == 2
        assert result.den == 5

    def test_div(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 / f2
        assert result.num == 8
        assert result.den == 9

    def test_str(self):
        f = Fraction(2, 5)
        assert str(f) == "2/5"

