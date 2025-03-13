def is_prime(n):
    """Überprüft, ob eine Zahl eine Primzahl ist."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def read_numbers_from_file(filename):
    """Liest eine Datei ein und gibt eine Liste von Zahlen zurück."""
    try:
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print("Fehler: Datei nicht gefunden.")
        return []
    except ValueError:
        print("Fehler: Datei enthält ungültige Werte.")
        return []

if __name__ == "__main__":
    filename = "numbers.txt"  # Datei mit den Zahlen
    numbers = read_numbers_from_file(filename)

    if numbers:
        for num in numbers:
            result = "ist eine Primzahl." if is_prime(num) else "ist keine Primzahl."
            print(f"{num} {result}")
