"""Tests for pimple."""

import pytest

import pimple


class TestRegex:
    """Test the regular expressions."""

    @pytest.mark.parametrize(
        "fname",
        [
            "test_pimple.py",
            "test_one.py",
            "test_test.py",
            "test_this_and_that.py",
            "test_1.py",
        ],
    )
    def test_re_python_file(self, fname):
        """Test the ``PYTHON_FILE`` regex:

        The ``PYTHON_FILE`` regex matches valid python files.
        """
        assert pimple.PYTHON_FILE.match(fname)

    @pytest.mark.parametrize(
        "fname",
        [
            "pimple.py",
            "setup.py",
            "README.md",
            "test_file.js",
            "test_1.pyc",
            "my_test_file.py",
            "Pipfile",
        ],
    )
    def test_re_python_file_invalid(self, fname):
        """Test the ``PYTHON_FILE`` regex:

        The ``PYTHON_FILE`` regex does not match invalid file names.
        """
        assert not pimple.PYTHON_FILE.match(fname)


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
