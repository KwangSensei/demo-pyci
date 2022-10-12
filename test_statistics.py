"""Unit test calculate functions for statistics.py."""
from math import sqrt
from unittest import TestCase
from statistics import variance, stdev


class StatisticsTest(TestCase):
    """Test statistics functions."""
    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_throws_exception(self):
        """Variance of an empty list should raise an exception."""
        with self.assertRaises(ValueError):
            var = variance([])

    def test_std_typical_values(self):
        """Standard deviation pf typical values."""
        self.assertEqual(0.0, stdev([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(sqrt(2.0), stdev([1, 2, 3, 4, 5]))
        self.assertEqual(sqrt(8.0), stdev([10, 2, 8, 4, 6]))


if __name__ == "__main__":
    import unittest
    unittest.main(verbosity=1)
