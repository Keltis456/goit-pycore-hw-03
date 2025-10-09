import random

def get_numbers_ticket(min, max, quantity):
    """
    Get a list of random numbers between min and max.
    min - minimum number
    max - maximum number
    quantity - quantity of numbers
    return: list of random numbers
    """
    if quantity > max - min:
        return []
    if quantity < 0:
        return []
    if min > max:
        return []
    if max - min < quantity:
        return []
    if min < 1:
        return []
    if max > 1000:
        return []
    try:
        return sorted(random.sample(range(min, max), quantity))
    except ValueError:
        return []

print(get_numbers_ticket(1, 10, 5))
print(get_numbers_ticket(1, 10, 10))
print(get_numbers_ticket(1, 10, 0))
print(get_numbers_ticket(1, 10, -1))
print(get_numbers_ticket(1, 10, 100))
print(get_numbers_ticket(1, 10, 1000))
print(get_numbers_ticket(1, 10, 10000))
print(get_numbers_ticket(1, 10, 100000))
print(get_numbers_ticket(1, 10, 1000000))
print(get_numbers_ticket(1, 10, 15))
print(get_numbers_ticket(1, 151, 150))