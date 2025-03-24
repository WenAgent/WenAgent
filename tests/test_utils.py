"""Unit tests for utility functions."""

import unittest
from src.utils import validate_input

class TestUtils(unittest.TestCase):
    """Test suite for utility functions."""

    def test_validate_input_valid(self):
        """Test valid input."""
        validate_input("What is this?")
        self.assertTrue(True)  # No exception raised

    def test_validate_input_invalid(self):
        """Test invalid input."""
        with self.assertRaises(ValueError):
            validate_input("")

if __name__ == "__main__":
    unittest.main()
