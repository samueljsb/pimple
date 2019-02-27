"""Tests for pimple."""

import pimple


class TestFormatting:
    """Test the string formatting functions."""

    def test_flush_left(self):
        """Test the ``flush_left`` function:

        Leading whitespace is removed from every line.
        Trailing whitespace is not removed.
        """
        input_ = "   line 1\nline 2\n          line 3    \n line 4"
        expected_output = "line 1\nline 2\nline 3    \nline 4"
        output = pimple.flush_left(input_)
        assert output == expected_output
