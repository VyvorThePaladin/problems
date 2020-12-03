# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

import unittest

# # -------- O(n) time and O(n) space ---------
# def find_unique_delivery_id(delivery_ids):

#     ids_to_occurrences = {}

#     for delivery_id in delivery_ids:
#         if delivery_id in ids_to_occurrences:
#             ids_to_occurrences[delivery_id] += 1
#         else:
#             ids_to_occurrences[delivery_id] = 1
    
#     for delivery_id, occurrences in list(ids_to_occurrences.items()):
#         if occurrences == 1:
#             return delivery_id

# ------------ O(n) time and O(1) space -----------
def find_unique_delivery_id(delivery_ids):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id


# How do you know when bit manipulation might be the key to solving a problem? Here are some signs to watch out for:

# You want to multiply or divide by 2 (use a left shift to multiply by 2, right shift to divide by 2).
# You want to "cancel out" matching numbers (use XOR).













# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)