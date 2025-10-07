from datetime import datetime

def get_days_from_today(date_string):
    """
    Get the number of days from today to a given date.
    """
    try:    
        today = datetime.now()
        date = datetime.strptime(date_string, "%Y-%m-%d")
        return (today - date).days
    except ValueError:
        return "Invalid date format"

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2026-10-09"))
print(get_days_from_today("2026-10-asf09"))