import pytest
import shapes

@pytest.mark.parametrize("side_lenght, expected_area", [(1,1), (2,4), (3,9), (4,16), (5,25)])
def test_multiple_square_areas(side_lenght, expected_area):
    assert shapes.Square(side_lenght).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(1, 4), (2, 8), (3, 12), (4, 16), (5, 20)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter