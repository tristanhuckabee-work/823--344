import pytest
from classes import RegularPolygon


def test_get_perimeter():
    tri = RegularPolygon(3,5)
    res = RegularPolygon.get_perimeter(tri)

    assert res == 15