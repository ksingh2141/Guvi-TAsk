from datetime import datetime


dt = datetime(2026, 3, 14)


extract_date = lambda d: (d.year, d.month, d.day)

print(extract_date(dt))