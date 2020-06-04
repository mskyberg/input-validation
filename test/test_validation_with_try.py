"""
Program: test_validation_with_try.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Test average calculation with mock input
"""

import unittest
import unittest.mock as mock
from input_validation import validation_with_try as avg


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            avg.average(-90, 89, 78)

    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            avg.average(90, -89, 78)

    def test_average_negative_input_score3(self):
        with self.assertRaises(ValueError):
            avg.average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()
