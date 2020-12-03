# Given a list of integers, find the highest product you can get from three of the integers.

# The input list_of_ints will always have at least three integers.

import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    # We could look at each integer thrice to get O(n^3) solution
    # We must look at each integer once so least possible is O(n) soln
    # Sorting is O(n lg n)
    # better soln is a greedy approach
    
    lowest_num = min(list_of_ints[0], list_of_ints[1])
    highest_num = max(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for i in range(2, len(list_of_ints)):
        current_num = list_of_ints[i]
        
        highest_product_of_3 = max(highest_product_of_3, \
            highest_product_of_2 * current_num, lowest_product_of_2 * current_num)
        
        highest_product_of_2 = max(highest_product_of_2, \
            current_num * highest_num, current_num * lowest_num)
        
        lowest_product_of_2 = min(lowest_product_of_2, \
            current_num * highest_num, current_num * lowest_num)
            
        lowest_num = min(lowest_num, current_num)
        highest_num = max(highest_num, current_num)


    return highest_product_of_3



















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)