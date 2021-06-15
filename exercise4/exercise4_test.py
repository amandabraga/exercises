from exercise4 import *
from unittest import mock
import pytest

class TestExercise4:

    # is_triangle tests

    def test_is_triangle_when_sides_are_equal_and_positive_should_return_true(self):
        sides = [4,4,4]
        assert is_triangle(sides) == True

    def test_is_triangle_when_sides_are_distinct_should_return_true(self):
        sides = [3,4,2]
        assert is_triangle(sides) == True

    @pytest.mark.parametrize("sides", [
        [0,0,0],
        [3,1,4],
        [3,4,1],
        [4,1,3]
    ])
    def test_is_triangle_when_sum_of_two_sides_is_not_bigger_than_other_side_should_return_false(self, sides):
        sides = [4,1,3]
        assert is_triangle(sides) == False
    
    @pytest.mark.parametrize("sides", [
        [-4,-4,-4],
        [-4,3,2],
        [4,-3,2],
        [4,3,-2]
    ])
    def test_is_triangle_when_sides_are_negative_should_return_false(self, sides):
        assert is_triangle(sides) == False
    
    
    # classify_triangles test

    def test_classify_triangles_when_side_values_are_invalid_should_return_not_a_triangle(self):
        expected = "Not a triangle"
        sides = [4,1,3]
        assert classify_triangles(sides) == expected

    @pytest.mark.parametrize("sides", [
        [4,4,3],
        [4,3,4],
        [3,4,4]
    ])
    def test_classify_triangles_when_two_of_the_sides_are_equal_should_return_isosceles(self, sides):
        expected = "Isosceles Triangle"
        assert classify_triangles(sides) == expected
    
    def test_classify_triangles_when_sides_are_distinct_should_return_scalene(self):
        expected = "Scalene Triangle"
        sides = [3,4,2]
        assert classify_triangles(sides) == expected
    
    def test_classify_triangles_when_sides_are_equal_should_return_equilateral(self):
        expected = "Equilateral Triangle"
        sides = [3,3,3]
        assert classify_triangles(sides) == expected
    

    # read_triangle_sides tests

    @mock.patch('builtins.input', side_effect=['11', '13', '12'])
    def test_read_triangle_when_values_are_valid_should_return_list(self, input):
        assert read_triangle_sides() == [11,13,12]
    
    @mock.patch('builtins.input', side_effect=['  11   ', ' 13 ', ' 12 '])
    def test_read_triangle_when_values_are_valid_but_contains_spaces_should_return_list(self, input):
        assert read_triangle_sides() == [11,13,12]
    
    @pytest.mark.parametrize("input_value", [
        ['', '11', '12'],
        ['11', '1a', '12'],
        ['11', '11', 'b2']
    ])
    def test_read_triangle_when_values_are_not_integer_should_raise_exception(self, input_value):
        with pytest.raises(ValueError):
            with mock.patch("builtins.input", side_effect = input_value):
                assert read_triangle_sides()