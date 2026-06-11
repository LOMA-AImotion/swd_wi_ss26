import unittest
from num_zeros import num_zeros


class TestNumZeros(unittest.TestCase):
    """Unit tests for the num_zeros function."""

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(num_zeros([]), 0)

    def test_no_zeros(self):
        """Test with a list containing no zeros."""
        self.assertEqual(num_zeros([1, 2, 3, 4, 5]), 0)

    def test_single_zero(self):
        """Test with a list containing a single zero."""
        self.assertEqual(num_zeros([0]), 1)

    def test_multiple_zeros(self):
        """Test with a list containing multiple zeros."""
        self.assertEqual(num_zeros([0, 0, 0]), 3)

    def test_zeros_mixed_with_integers(self):
        """Test with zeros mixed among other integers."""
        self.assertEqual(num_zeros([1, 0, 2, 0, 3, 0]), 3)

    def test_negative_integers(self):
        """Test with negative integers and zeros."""
        self.assertEqual(num_zeros([-1, 0, -2, 0, -3]), 2)

    def test_large_integers(self):
        """Test with large integers and zeros."""
        self.assertEqual(num_zeros([1000, 0, 2000, 0]), 2)

    def test_all_zeros(self):
        """Test with a list of all zeros."""
        self.assertEqual(num_zeros([0, 0, 0, 0, 0]), 5)

    def test_zero_at_start(self):
        """Test with zero at the start of the list."""
        self.assertEqual(num_zeros([0, 1, 2, 3]), 1)

    def test_zero_at_end(self):
        """Test with zero at the end of the list."""
        self.assertEqual(num_zeros([1, 2, 3, 0]), 1)


if __name__ == '__main__':
    unittest.main()
