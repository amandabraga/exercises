from exercise3 import *
import pytest

class TestExercise3:

    # reverse_and_format tests

    @pytest.mark.parametrize(
        "name, expected", 
        [  ("John", "nhoJ"),
           ("a", "A"),
           ("wu Doe", "eoD uW"),
           ("john doe", "eoD nhoJ"),
           ("", ""),
           ("a b", "B A"),
           ("   ", ""),
           (" Lia Silva", "avliS aiL")
        ]
    )
    def test_reverse_and_format_when_name_is_valid_should_return_reversed_string(self, name, expected):
        assert reverse_and_format(name) == expected

    @pytest.mark.parametrize(
        "name", 
        [  [1],
           15.9,
           { "a": "name" }
        ]
    )
    def test_reverse_and_format_when_name_is_not_string_should_raise_error(self, name):
        with pytest.raises(TypeError):
            assert reverse_and_format(name)

    # last_char_is_a_space tests

    @pytest.mark.parametrize(
        "name, index", 
        [  ("na me", 3),
           ("  ", 1)
        ]
    )
    def test_last_char_is_a_space_when_last_char_is_space_should_return_true(self, name, index):
        assert last_char_is_a_space(name, index) == True

    @pytest.mark.parametrize(
        "name, index", 
        [  ("na me", 1),
           ("name", 2),
           ("  ", 0)
        ]
    )
    def test_last_char_is_a_space_when_last_char_is_space_should_return_false(self, name, index):
        assert last_char_is_a_space(name, index) == False
    
    @pytest.mark.parametrize(
        "name, index", 
        [  ("name", 10) ]
    )
    def test_last_char_is_a_space_when_index_is_invalid_should_raise_error(self, name, index):
        with pytest.raises(IndexError):
            last_char_is_a_space(name, index)