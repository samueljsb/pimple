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


class TestCollection:
    """Tests for the collection of test modules, classes, and functions."""

    def test_import_module(self, tmpdir):
        """Test that a module can be imported."""
        test_file = tmpdir.join("test_file.py")
        test_file.write(
            '"""This is a test module."""\n'
            "\n"
            "def foo():\n"
            "    pass\n"
            "\n"
            "class Bar:\n"
            "    pass\n"
        )

        module = pimple.import_module(test_file)
        assert module.__doc__ == "This is a test module."
        assert "foo" in dir(module)
        assert "Bar" in dir(module)
