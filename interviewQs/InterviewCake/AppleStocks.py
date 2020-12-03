# Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

# For example:

#   stock_prices = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices)
# # Returns 6 (buying for $5 and selling for $11)

# # ---------- O(N^2) SOLUTION ------------
# def get_max_profit(stock_prices):

#     # Calculate the max profit
#     max_profit = 0
    
#     if len(stock_prices) <= 1:
#         raise Exception
    
#     for earlier_time, earlier_price in enumerate(stock_prices):
#         for later_time in range(earlier_time + 1,len(stock_prices)):
            
#             later_price = stock_prices[later_time]
                           
#             potential_profit = later_price - earlier_price
            
#             max_profit = max(potential_profit, max_profit)

#     return max_profit

def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('Need two values atleast to turn a profit or loss.')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in range(1, len(stock_prices)):

        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    return max_profit










# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)