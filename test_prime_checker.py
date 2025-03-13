import unittest
from prime_checker import is_prime, read_numbers_from_file
import os

class TestPrimeChecker(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(100))

    def test_negative_and_zero(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(0))

class TestFileReading(unittest.TestCase):
    def setUp(self):
        """Erstellt eine temporäre Datei für Tests."""
        self.test_filename = "test_numbers.txt"
        with open(self.test_filename, "w") as f:
            f.write("2\n3\n4\n5\n6\n")

    def test_read_numbers_from_file(self):
        """Testet, ob die Zahlen korrekt eingelesen werden."""
        expected_numbers = [2, 3, 4, 5, 6]
        self.assertEqual(read_numbers_from_file(self.test_filename), expected_numbers)

    def tearDown(self):
        """Löscht die Testdatei nach dem Test."""
        os.remove(self.test_filename)

if __name__ == "__main__":
    unittest.main()
