import unittest

from isPalindrome import isPalindrome

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_with_spaces_and_punctuation(self):
        self.assertTrue(isPalindrome("Was it a car or a cat I saw?"))

    def test_not_palindrome(self):
        self.assertFalse(isPalindrome("tab a cat"))

    def test_single_character(self):
        self.assertTrue(isPalindrome("a"))

    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))

    def test_case_sensitivity(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))

    def test_non_alphanumeric_characters(self):
        self.assertTrue(isPalindrome("Able was I ere I saw Elba!"))

if __name__ == '__main__':
    unittest.main()