from utils import is_power_of_two

def main():
    numbers = [1, 2, 8, 10, 16, 20, 0, -2]
    
    print("--- Перевірка степенів двійки ---")
    for num in numbers:
        result = is_power_of_two(num)
        print(f"Чи є число {num} степенем двійки? -> {result}")

if __name__ == "__main__":
    main()


prime_number = 7
print(f"Чи є число {prime_number} простим? {is_prime(prime_number)}")

from utils import is_odd
