from dateutil import parser
from datetime import datetime, timezone, timedelta


def parse_date(date_str):
    """
    Parse the date string using dateutil.parser and return a timezone-aware datetime object.
    """
    date_obj = parser.parse(date_str)
    if date_obj.tzinfo is None:
        date_obj = date_obj.replace(
            tzinfo=timezone.utc)  # Or replace with the correct timezone
    return date_obj


# Define date strings
date_str1 = "2024-09-07T12:11:31.212307Z"  # Example with timezone
date_str2 = "2024-09-05 14:30:00"  # Example without timezone
date_str3 = "2026-02-28T05:00:00Z"
open_date = "2024-09-06"

# Convert strings to timezone-aware datetime objects
date_obj1 = parse_date(date_str1)
date_obj2 = parse_date(date_str2)
date_obj3 = parse_date(date_str3)
date_obj4 = parse_date(open_date)

# Get the current time in UTC
now = datetime.now(timezone.utc)
print("Current time in UTC:", now)

# Extract only the date from each datetime object
date_only_now = now.date()
date_only_obj1 = date_obj1.date()
date_only_obj2 = date_obj2.date()
date_only_obj3 = date_obj3.date()
date_only_obj4 = date_obj4.date()

# Calculate differences based on the date only (ignoring time)
diff1_in_days = (date_only_obj1 - date_only_now).days
diff2_in_days = (date_only_obj2 - date_only_now).days
diff3_in_days = (date_only_obj3 - date_only_now).days
diff4_in_days = (date_only_obj4 - date_only_now).days

print("Difference with date 1 in days (date only):", diff1_in_days)
print("Difference with date 2 in days (date only):", diff2_in_days)
print("Difference with date 3 in days (date only):", diff3_in_days)
print("Difference with date 4 in days (date only):", diff4_in_days)

# Calculate the after grace period (10 days from today)
after_grace_period = (datetime.today() +
                      timedelta(days=10)).strftime('%Y-%m-%d')
print(after_grace_period, type(after_grace_period))

ten_days_ago = (date_only_now - timedelta(days=10))
print(ten_days_ago,"adkf",type(ten_days_ago))
print((date_only_obj4 - ten_days_ago).days)
# maturity_date_difference_in_days in range(
# -maturity_days_limit, 1) if maturity_days_limit > 0 else maturity_date_difference_in_days in range(0, abs(maturity_days_limit)+1)

print(f"{date_only_obj4} < {ten_days_ago} = {date_only_obj4<ten_days_ago}")