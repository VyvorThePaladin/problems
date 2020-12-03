# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.

# For example:
# message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]

# reverse_words(message)

# # Prints: 'steal pound cake'
# print(''.join(message))

import unittest


def reverse_words(message):

    # First reverse the entire sentence
    reverse_chars(message, 0, len(message) - 1)

    # Next reverse the words in place
    word_left_index = 0
    for i in range(len(message) + 1):
        if (i == len(message)) or (message[i] == ' '):
            reverse_chars(message, word_left_index, i - 1)
            word_left_index = i + 1

def reverse_chars(msg, left_index, right_index):
    while left_index < right_index:
        msg[left_index], msg[right_index] = msg[right_index], msg[left_index]
        left_index += 1
        right_index -= 1

# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)