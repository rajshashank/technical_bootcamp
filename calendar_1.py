import calendar


def print_calendar(month, year):
    # Create a calendar for the given month and year
    cal = calendar.monthcalendar(year, month)

    # Print the header for the calendar
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")  # Weekday headers

    # Print each week in the month
    for week in cal:
        print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))


# Example usage:
month = 9
year = 2024
print_calendar(month, year)
