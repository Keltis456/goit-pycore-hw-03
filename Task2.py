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
        return "Quantity is greater than the range"
    if quantity < 0:
        return "Quantity is less than 0"
    if min > max:
        return "Minimum number is greater than maximum number"
    if max - min < quantity:
        return "Quantity is greater than the range"
    if min < 1:
        return "Minimum number is less than 1"
    if max > 1000:
        return "Maximum number is greater than 1000"
    try:
        return sorted(random.sample(range(min, max), quantity))
    except ValueError:
        return "Invalid quantity"

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