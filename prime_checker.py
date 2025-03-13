def is_prime(n):
    """Checks if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def read_numbers_from_file(filename):
    """Reads a file and returns a list of numbers."""
    try:
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except ValueError:
        print("Error: File contains invalid values.")
        return []


if __name__ == "__main__":
    filename = "numbers.txt"  # File containing the numbers
    numbers = read_numbers_from_file(filename)

    if numbers:
        for num in numbers:
            result = (
                "is a prime number."
                if is_prime(num)
                else "is not a prime number."
            )
            print(f"{num} {result}")

