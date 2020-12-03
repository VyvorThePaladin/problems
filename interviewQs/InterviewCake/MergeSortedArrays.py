#  Write a function to merge lists of integers into one sorted list.
# For example:

# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(merge_lists(my_list, alices_list))

import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    
    # First create a merged list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size
    
    # Create three indices to track progress
    my_head_index = 0
    alices_head_index = 0
    merged_head_index = 0
    
    while merged_head_index < merged_list_size:
        # Set flags
        is_my_list_exhausted = my_head_index >= len(my_list)
        is_alices_list_exhausted = alices_head_index >= len(alices_list)

        if (not is_my_list_exhausted) and (is_alices_list_exhausted or \
                my_list[my_head_index] < alices_list[alices_head_index]):
            # Case: my list is not exhausted AND
            #           1) alices list is exhausted OR
            #           2) my list is next
            merged_list[merged_head_index] = my_list[my_head_index]
            my_head_index += 1
        else:
            merged_list[merged_head_index] = alices_list[alices_head_index]
            # Case: alices list is next
            alices_head_index += 1
        merged_head_index += 1
        
    return merged_list











# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)