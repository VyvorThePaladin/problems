# We have a list of integers, where:
#   1. The integers are in the range 1..n
#   2. The list has a length of n+1
# It follows that our list has at least one integer which appears at least twice. 
# But it may have several duplicates, and each duplicate may appear more than twice.

# Write a function which finds an integer that appears more than once in our list. 
# (If there are multiple duplicates, you only need to find one of them.)

# GOAL: reduce space

import unittest

# # -------------- O(n) space and time --------------
# def find_repeat(numbers):
#     numbers_seen = set()
#     for number in numbers:
#         if number in numbers_seen:
#             return number
#         else:
#             numbers_seen.add(number)
    
#     raise Exception('no duplicate')

# # -------------- O(1) space and O(n^2) time --------------
# def find_repeat(numbers):
    
#     for needle in range(1, len(numbers)):
#         has_been_seen = False
#         for number in numbers:
#             if needle == number:
#                 if has_been_seen:
#                     return number
#                 else:
#                     has_been_seen = True
    
#     raise Exception('no duplicates!')

# -------------- O(1) space and O(n log n) time --------------
def find_repeat(numbers):

    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        midpoint = floor + ((ceiling - floor) // 2)
        # split into upper range and lower range
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # count number of items in lower range
        number_of_possible_items_in_lower_range = 0
        for number in numbers:
            if number >= lower_range_floor and number <= lower_range_ceiling:
                number_of_possible_items_in_lower_range += 1
        
        # check if duplicate in lower range or upper range
        number_of_all_items_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if number_of_possible_items_in_lower_range > number_of_all_items_in_lower_range:
            # duplicate in lower range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # duplicate in upper range
            floor, ceiling = upper_range_floor, upper_range_ceiling
    
    # both ceiling and floor have collapsed into each other
    return floor
























# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)