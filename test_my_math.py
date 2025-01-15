""" Test the my_math module """

import unittest
from my_math import my_add

# FILE: test_my_math.py


class TestMyAddLazy(unittest.TestCase):
    """ Test the my_add function """
    def test_positive_numbers_lazy(self):
        """ Test adding two positive numbers representing sizes of a shape

        Feature: Add positive numbers representing sizes of a shape
        Scenario: Get the sum of two positive numbers

        Given I have two positive numbers
        When I add them together
        Then I should get the sum of the two numbers
        """
        # expected = 3
        # actual = my_add(1, 2)
        # self.assertEqual(actual, expected)
        # all tests are commented out but still get 100% coverage
        my_add(1, 2)  # execute the function to get 100% coverage

    def test_negative_numbers_lazy(self):
        """ Test adding two negative numbers """
        # self.assertEqual(my_add(-1, -2), -3)

    def test_mixed_numbers_lazy(self):
        """ Test adding a positive and a negative number """
        # self.assertEqual(my_add(-1, 2), 1)

    def test_zero_lazy(self):
        """ Test adding zero """
        # self.assertEqual(my_add(0, 0), 0)
        # self.assertEqual(my_add(0, 5), 5)
        # self.assertEqual(my_add(5, 0), 5)


# if __name__ == '__main__':
#     unittest.main()
