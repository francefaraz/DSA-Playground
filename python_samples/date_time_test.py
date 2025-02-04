from dateutil import parser
from datetime import datetime, timezone ,timedelta

def parse_date(date_str):
    """
    Parse the date string using dateutil.parser and return a timezone-aware datetime object.
    """
    # Parse the date string
    date_obj = parser.parse(date_str)

    # If the parsed date is naive (i.e., has no timezone information), make it timezone-aware
    if date_obj.tzinfo is None:
        # Assuming local timezone if naive (adjust if necessary)
        date_obj = date_obj.replace(tzinfo=timezone.utc)  # Or replace with the correct timezone

    return date_obj

# Define date strings
date_str1 = "2024-09-07T12:11:31.212307Z"  # Example with timezone
date_str2 = "2024-09-05 14:30:00"        # Example without timezone
date_str3 = "2026-02-28T05:00:00Z"
open_date=  "2024-09-07"

# Convert strings to timezone-aware datetime objects
date_obj1 = parse_date(date_str1)
date_obj2 = parse_date(date_str2)
date_obj3 = parse_date(date_str3)
date_obj4 = parse_date(open_date)
# Get the current time in UTC
now = datetime.now(timezone.utc)
print(now)

print("Current time in UTC:", now)
print("Parsed date 1:", date_obj1)
print("Parsed date 2:", date_obj2)
print("Parsed date 3:", date_obj3)
print("Parsed date 4:", date_obj4)

# Calculate differences
diff1 = date_obj1 - now
diff2 = date_obj2 - now
diff3= date_obj3 - now
diff4 = date_obj4 - now

print("Difference with date 1 in days:", diff1.days)
print("Difference with date 2 in days:", diff2.days)
print("Difference with date 3 in days:", diff3.days)
print("Difference with date 4 in days:", diff4.days)


after_grace_period = (datetime.today()+timedelta(days=10)).strftime('%Y-%m-%d')

print(after_grace_period, type(after_grace_period))


