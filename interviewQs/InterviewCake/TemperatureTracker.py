# Write a class TempTracker with these methods:

# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean of all temps we've seen so far
# get_mode()—returns a mode of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

# get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.

# If there is more than one mode, return any of the modes.

import unittest

class TempTracker(object):
    def __init__(self):
        # store max and min temperature
        self.max_temp = float('-inf')
        self.min_temp = float('inf')

        # for mean
        self.number_of_records = 0
        self.mean = None
        self.total_sum_of_temps = 0.0

        # for mode
        self.all_possible_temperatures = [0] * 111
        self.mode = 0
        self.max_possible_occurences = 0

    def insert(self, temperature):
        # compute mode
        self.all_possible_temperatures[temperature] += 1
        if self.all_possible_temperatures[temperature] > self.max_possible_occurences:
            self.mode = temperature
            self.max_possible_occurences = self.all_possible_temperatures[temperature]


        # compute mean
        self.number_of_records += 1
        self.total_sum_of_temps += temperature
        self.mean = self.total_sum_of_temps/self.number_of_records

        # set min and max temperature
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode











# Tests
class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)