import re

def normalize_phone(phone_number):
    """
    Normalize a phone number.
    Remove all non-digit and spaces characters except for the first '+'.
    If number starts with '38', add '+'.
    If number doesn't start with '+38', add '+38'.
    """
    normalized_phone = re.sub(r'[^0-9+]', '', phone_number)
    if normalized_phone.startswith('38'):
        normalized_phone = "+" + normalized_phone
    if not normalized_phone.startswith('+38'):
        normalized_phone = "+38" + normalized_phone
    return normalized_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+380(67)777-7-777",
    "+38(067)777-7-777",
    "+380677777777",
    "+380(67)777-7-777",
    "+380(67)777-7-777",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


