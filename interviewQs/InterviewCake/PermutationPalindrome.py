# Write an efficient function that checks whether any permutation of an input string is a palindrome.

# You can assume the input string only contains lowercase letters.

# Examples:

# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False

import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    # palindrome can have only one unique char, rest must be in pairs
    unpaired_char = set()

    for char in the_string:
        if char in unpaired_char:
            unpaired_char.remove(char)
        else:
            unpaired_char.add(char)

    return len(unpaired_char) <= 1














# Tests
class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)