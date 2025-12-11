import math
import os
import sys
from typing import Any

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from lab1oop.task_package_1.zad1 import Kalor, make_Point


class TestKalor:
    def test_initialization_valid(self) -> None:
        k = Kalor(250, 0.35)
        assert k.first == 250
        assert k.second == 0.35

    def test_initialization_invalid_type(self) -> None:
        with pytest.raises(ValueError):
            Kalor("abc", 0.3)  # type: ignore

    def test_initialization_non_positive(self) -> None:
        with pytest.raises(ValueError):
            Kalor(0, 0.5)
        with pytest.raises(ValueError):
            Kalor(200, -1.0)

    def test_power_calculation(self) -> None:
        # 250 ккал на 100 г, масса 0.35 кг -> 250 * 0.35 * 10 = 875
        k = Kalor(250, 0.35)
        assert k.power() == pytest.approx(875.0)

    def test_display_output(self, capsys: Any) -> None:
        k = Kalor(300, 0.5)
        k.display()
        captured = capsys.readouterr()
        assert "Калорийность 100 г: 300" in captured.out
        assert "масса продукта: 0.5 кг" in captured.out

    def test_power_and_Power_same(self) -> None:
        k = Kalor(100, 1.0)
        assert k.power() == k.Power() == pytest.approx(1000.0)


class TestMakePoint:
    def test_make_point_valid(self) -> None:
        obj = make_Point(200, 0.4)
        assert isinstance(obj, Kalor)
        assert obj.first == 200
        assert obj.second == 0.4

    def test_make_point_invalid(self) -> None:
        # make_Point при ошибке должен завершить программу
        with pytest.raises(SystemExit):
            make_Point(-10, 0.3)
