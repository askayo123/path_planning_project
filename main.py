import random

def generate_random_numbers(count, lower=1, upper=100):
    return [random.randint(lower, upper) for _ in range(count)]

if __name__ == "__main__":
    numbers = generate_random_numbers(10)
    print("Random numbers:", numbers)