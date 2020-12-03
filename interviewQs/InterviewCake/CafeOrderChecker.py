# Given three order lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

# We'll represent each customer order as a unique integer.

# As an example,

#   Take Out Orders: [1, 3, 5]
#  Dine In Orders: [2, 4, 6]
#   Served Orders: [1, 2, 4, 6, 5, 3]
# would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

# But,

#   Take Out Orders: [17, 8, 24]
#  Dine In Orders: [12, 19, 2]
#   Served Orders: [17, 8, 12, 19, 24, 2]
# would be first-come, first-served.



import unittest


# ------------- O(n^2) DUE TO ARRAY SLICES -------------
# def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # base case
    # if len(served_orders) == 0:
    #     return True

    # if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
    #     return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])

    # elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
    #     return is_first_come_first_served(take_out_orders, dine_in_orders[1:], served_orders[1:])

    # else:    
    #     return False

    # more optimized solution

    

# def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders, take_out_order_index=0, dine_in_order_index=0, served_order_index=0):

#     # base case
#     if served_order_index == len(served_orders):
#         return True
        
#     # Parse current values
#     if take_out_order_index < len(take_out_orders) and served_orders[served_order_index] == take_out_orders[take_out_order_index]:
#         take_out_order_index += 1
#     elif dine_in_order_index < len(dine_in_orders) and served_orders[served_order_index] == dine_in_orders[dine_in_order_index]:
#         dine_in_order_index += 1
#     else:
#         return False
    
#     # Move to next index
#     served_order_index += 1
#     return is_first_come_first_served(take_out_orders, dine_in_orders, served_orders, take_out_order_index, dine_in_order_index, served_order_index)

# ------------- ITERATIVE METHOD TAKING O(n) TIME & O(1) ADDITIONAL SPACE -------------
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_order_index = 0
    dine_in_order_index = 0
    max_take_out_order_index = len(take_out_orders) - 1
    max_dine_in_order_index = len(dine_in_orders) - 1
    
    for order in served_orders:
        if take_out_order_index <= max_take_out_order_index and \
            order == take_out_orders[take_out_order_index]:
            take_out_order_index += 1
        
        elif dine_in_order_index <= max_dine_in_order_index and \
            order == dine_in_orders[dine_in_order_index]:
                dine_in_order_index += 1
        
        else:
            return False
    
    if take_out_order_index != len(take_out_orders) or \
        dine_in_order_index != len(dine_in_orders):
            return False
   
    return True




















# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)