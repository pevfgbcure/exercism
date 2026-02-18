from math import isqrt


def prime(number: int) -> int:
    """Returns the nth prime number.

    Args:
        number (int): The position of the prime number to return (1-based index).

    Returns:
        int: The nth prime number.

    Raises:
        ValueError: If the input number is less than 1.
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")

    primes_found = 0
    current_number = 2
    while primes_found < number:
        if is_prime(current_number):
            primes_found += 1
        current_number += 1

    return current_number - 1


def is_prime(n) -> bool:
    """Checks if a number is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True
