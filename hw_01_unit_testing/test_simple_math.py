import pytest
from simple_math import SimpleMath


@pytest.fixture
def math():
    """Create a SimpleMath instance for each test."""
    return SimpleMath()


class TestSquare:
    """Tests for the square() method."""

    def test_square_positive(self, math):
        """square(2) should return 4."""
        assert math.square(2) == 4

    def test_square_negative(self, math):
        """square(-3) should return 9."""
        assert math.square(-3) == 9

    def test_square_zero(self, math):
        """square(0) should return 0."""
        assert math.square(0) == 0

    def test_square_one(self, math):
        """square(1) should return 1."""
        assert math.square(1) == 1

    def test_square_large(self, math):
        """square(10) should return 100."""
        assert math.square(10) == 100


class TestCube:
    """Tests for the cube() method."""

    def test_cube_positive(self, math):
        """cube(2) should return 8."""
        assert math.cube(2) == 8

    def test_cube_negative(self, math):
        """cube(-3) should return -27."""
        assert math.cube(-3) == -27

    def test_cube_zero(self, math):
        """cube(0) should return 0."""
        assert math.cube(0) == 0

    def test_cube_one(self, math):
        """cube(1) should return 1."""
        assert math.cube(1) == 1

    def test_cube_large(self, math):
        """cube(10) should return 1000."""
        assert math.cube(10) == 1000
