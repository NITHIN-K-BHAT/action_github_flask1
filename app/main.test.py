from main import return_backwards_string
import unittest
import os


class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "kannada is malayalam"
        return_backwards_string = "malayalam si adannak"
        self.assertEqual(return_backwards_string, return_backwards_string(random_string))

if __name__ == "__main__":
    unittest.main()
