import gcdString
import unittest

class gcdStringMethods(unittest.TestCase):

    def test_standard_input(self):
        self.assertEqual(gcdString.Solution.gcdOfStrings('ababab', 'abab'), 'ab')

    def test_no_match(self):
        self.assertEqual(gcdString.Solution.gcdOfStrings('LEET', 'CODE'), "")


if __name__ == "main":
    unittest.main()