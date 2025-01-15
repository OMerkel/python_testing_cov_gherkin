""" Test the my_math module """

import math
import unittest
from my_math import my_add

# FILE: test_my_math.py


class TestMyAddCorrect(unittest.TestCase):
    """ Test the my_add function """
    def test_positive_numbers(self):
        """ Test adding two positive numbers

        test type: Positive test

        Feature: Add positive numbers
        Scenario: Get the sum of two positive numbers

        Given I have two positive numbers
        When I add them together as a user of the function
        Then I should get the sum of the two numbers in order to...

        Sample of how to write a Gherkin incorporating
        a agile User Story description and acceptance criteria
        """
        expected = 3
        actual = my_add(1, 2)
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        """ Test adding two negative numbers representing sizes of a shape

        test type: boundary test

        mind: There is no negative size for a shape

        Feature: Add negative numbers representing sizes of a shape
        Scenario: Get the sum of two negative numbers

        Given I have two negative numbers representing sizes of a shape
        When I add them together
        Then I should get the a NaN value
        """
        expected = float('nan')
        actual = my_add(-1, -2)
        self.assertTrue(math.isnan(expected) and math.isnan(actual))

    def test_mixed_numbers(self):
        """ Test adding a positive and a negative number representing sizes

        test type: Negative test

        Feature: Add a positive and a negative number representing sizes
        Scenario: Get the sum of a positive and a negative number

        Given I have a positive and a negative number
        When I add them together
        Then I should get a NaN value since that addition is not defined
        """
        self.assertTrue(math.isnan(float('nan')) and math.isnan(my_add(-1, 2)))

    def test_zero(self):
        """ Test adding zero

        test type: sanity test

        Feature: Add zero as a neutral element
        Scenario: Get the sum of a number and zero

        Given I have a number and zero
        When I add the number and zero
        Then I should get the number
        """
        self.assertEqual(my_add(0, 0), 0)
        self.assertEqual(my_add(0, 5), 5)
        self.assertEqual(my_add(5, 0), 5)


# if __name__ == '__main__':
#     unittest.main()
