import unittest
from urlify import urlify

class Test_Case_Urlify(unittest.TestCase):
    def test_urlify(self):
        self.assertEqual(urlify("", 0), "")
        self.assertEqual(urlify("Hi there", 8), "Hi%20there")
        self.assertEqual(urlify("Hi  there", 9), "Hi%20%20there")
        self.assertEqual(urlify("  ", 2), "%20%20")
        self.assertEqual(urlify("hey whats up", 12), "hey%20whats%20up")

if __name__ == "__main__":
    unittest.main()