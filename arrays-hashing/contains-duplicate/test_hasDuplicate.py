from hasDuplicate import hasDuplicate

import unittest

class TestHasDuplicate(unittest.TestCase):
    def test_duplicate_present(self):
        nums = [1, 2, 3, 3]
        self.assertTrue(hasDuplicate(nums))

    def test_no_duplicate(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(hasDuplicate(nums))

    def test_empty_list(self):
        nums = []
        self.assertFalse(hasDuplicate(nums))

    def test_single_element(self):
        nums = [1]
        self.assertFalse(hasDuplicate(nums))

if __name__ == '__main__':
    unittest.main()