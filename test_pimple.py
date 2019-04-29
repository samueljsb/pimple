"""Tests for pimple."""

import pimple


class TestFormatting:
    """Test the string formatting functions."""

    def test_flush_left(self):
        """Test the ``flush_left`` function:

        Leading whitespace is removed from every line.
        Trailing whitespace is not removed.
        """
        input_ = """This is an example docstring.

            The first line is not indented, but the
            remaining lines need to be dedented.

            But:
                1) subsequent indentation should not be lost
                2) newlines should not be lost.
        """
        expected_output = (
            "This is an example docstring.\n"
            "\n"
            "The first line is not indented, but the\n"
            "remaining lines need to be dedented.\n"
            "\n"
            "But:\n"
            "    1) subsequent indentation should not be lost\n"
            "    2) newlines should not be lost.\n"
        )
        output = pimple.flush_left(input_)
        assert output == expected_output
