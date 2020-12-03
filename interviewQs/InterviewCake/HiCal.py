# Our company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.

# To do this, you’ll need to know when any team is having a meeting. 
# In HiCal, a meeting is stored as a tuple of integers (start_time, end_time). 
# These integers represent the number of 30-minute blocks past 9:00am.

# Write a function merge_ranges() that takes a list of multiple meeting time ranges and 
# returns a list of condensed ranges.
# For example, given:
#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# your function would return:
#   [(0, 1), (3, 8), (9, 12)]

import unittest

def merge_ranges(meetings):

    # Merge meeting ranges
    sorted_meetings = sorted(meetings)

    merged_meetings = [sorted_meetings[0]]

    for current_start, current_end in sorted_meetings[1:]:
        last_merged_start, last_merged_end = merged_meetings[-1]

        if current_start <= last_merged_end:
            merged_meetings[-1] = (last_merged_start, max(current_end, last_merged_end))
        
        else:
            merged_meetings.append((current_start, current_end))

    return merged_meetings


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)