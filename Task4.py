from datetime import datetime

users = [
    {"name": "Jim Beam", "birthday": "1995.08.15"},
    {"name": "John Doe", "birthday": "1985.10.13"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Lane Smith", "birthday": "1990.10.9"},
]

"""
Format of birthday: "YYYY.MM.DD"
Parse birthday to datetime object.
Get the upcoming birthdays from a list of users. For next 7 days.
users - list of users
return: list of upcoming birthdays
"""
def get_upcoming_birthdays(users):
    today = datetime.today()
    current_year = today.year
    upcoming = []
    for user in users:
        # Parse the birthday string to a datetime object
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        # Set the birthday to this year
        bday_this_year = bday.replace(year=current_year)
        # If birthday already passed this year, set to next year
        if bday_this_year < today:
            bday_next = bday.replace(year=current_year + 1)
            days_until = (bday_next - today).days
        else:
            days_until = (bday_this_year - today).days
        if 0 <= days_until < 7:
                upcoming.append(user)
    return upcoming

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
