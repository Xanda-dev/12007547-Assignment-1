import unittest
import os
from prime_checker import is_prime, read_numbers_from_file


class TestPrimeChecker(unittest.TestCase):
    def test_prime_numbers(self):
        """Test with actual prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for num in primes:
            self.assertTrue(is_prime(num))

    def test_non_prime_numbers(self):
        """Test with non-prime numbers."""
        non_primes = [0, 1, 4, 6, 8, 9, 10, 15]
        for num in non_primes:
            self.assertFalse(is_prime(num))

    def test_large_prime(self):
        """Test a large prime number."""
        self.assertTrue(is_prime(7919))  # 7919 is a known prime number

    def test_large_non_prime(self):
        """Test a large non-prime number."""
        self.assertFalse(is_prime(8000))  # 8000 is divisible by 2

    def test_read_numbers_from_file(self):
        """Test if reading numbers from a file works correctly."""
        test_filename = "test_numbers.txt"

        try:
            # Create a sample file
            with open(test_filename, "w") as f:
                f.write("2\n3\n4\n5\n")

            # Test the function
            numbers = read_numbers_from_file(test_filename)
            self.assertEqual(numbers, [2, 3, 4, 5])

        finally:
            # Delete the file after the test
            if os.path.exists(test_filename):
                os.remove(test_filename)


if __name__ == "__main__":
    unittest.main()
