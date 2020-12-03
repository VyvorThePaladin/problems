# Write a function that takes:

# a list of unsorted_scores
# the highest_possible_score in the game
# and returns a sorted list of scores in less than O(nlgn) time.

# For example:

#   unsorted_scores = [37, 89, 41, 65, 91, 53]
# HIGHEST_POSSIBLE_SCORE = 100

# # Returns [91, 89, 65, 53, 41, 37]
# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    # O(n log n) must be beaten -> O(n)
    # Use greedy or counting 
    # using counting sort
    
    # List of zeroes     
    score_counts = [0] * (highest_possible_score + 1)
    
    # Populate score counts
    for score in unsorted_scores:
        score_counts[score] += 1
        
    # Populate final sorted list
    sorted_scores = []
    
    # For each item in score counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]
        
        # For the number of times the item occurs
        for time in range(count):
            # add it to sorted scores list
            sorted_scores.append(score)

    return sorted_scores


















# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)