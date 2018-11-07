import unittest #the test package we use
from order_verify import check_order_status

class TestOrder(unittest.TestCase):
    def test_order_status(self): # start with test as a convention, assert means check if
        self.assertEqual(check_order_status(3), False)
        self.assertFalse(check_order_status(3), False)

    def test_id_is_integer(self):
        self.assertIsInstance(check_order_status(3), int)

    def test_id_does_not_exist_in_both_lists(self):
        self.assertFalse(check_order_status(3), False)
    
    def test_if_there_are_orders_added_to_the_list(self):
        self.assertFalse(check_order_status(5), False)

    # def test_for_adding_a_new_order(self):
    #     self.assertEqual(check_order_status(7), True)

    def test_for_making_an_order_delivered(self):
        self.assertEqual(check_order_status(1), True)