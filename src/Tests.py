from Helpers import *
from Algorithms import *
import unittest

class test_is_sorted(unittest.TestCase):

    def test_is_sorted_returns_false(self):
        array = [5, 3, 2, 1]
        array_2 = [1,2,4,3,5]
        array_3 =  [1,1,1,1,1,1,1,2,3,4,1,3]

        self.assertFalse(is_sorted(array))
        self.assertFalse(is_sorted(array_2))
        self.assertFalse(is_sorted(array_3))
    
    def test_is_sorted_returns_true(self):
        array = [1,2,3,4]
        array_2 = [0]
        array_3 = [1,15,24,44,55,100]

        self.assertTrue(is_sorted(array))
        self.assertTrue(is_sorted(array_2))
        self.assertTrue(is_sorted(array_3))

class test_selection_sort(unittest.TestCase):

    def test_selection_sort_presorted_array(self):
        array = [1,2,3,4,5]
        self.assertTrue(is_sorted(array))
        selection_sort(array)
        self.assertTrue(is_sorted(array))

    def test_selection_sort_unsorted_array(self):
        array = [5,4,3,2,1]
        self.assertFalse(is_sorted(array))
        selection_sort(array)
        self.assertTrue(is_sorted(array))

class test_bubble_sort(unittest.TestCase):

    def test_bubble_sort_presorted_array(self):
        array = [1,2,3,4,5]
        self.assertTrue(is_sorted(array))
        bubble_sort(array)
        self.assertTrue(is_sorted(array))

    def test_bubble_sort_unsorted_array(self):
        array = [5,4,3,2,1]
        self.assertFalse(is_sorted(array))
        bubble_sort(array)
        self.assertTrue(is_sorted(array))

class test_hayes_sort(unittest.TestCase):

    def test_selection_sort_presorted_array(self):
        array = [1,2,3,4,5]
        self.assertTrue(is_sorted(array))
        actual = hayes_sort(array)
        self.assertTrue(is_sorted(actual))

    def test_hayes_sort_unsorted_array(self):
        array = [5,4,3,2,1]
        self.assertFalse(is_sorted(array))
        actual = hayes_sort(array)
        self.assertTrue(is_sorted(actual))
if __name__ == '__main__':
    unittest.main()