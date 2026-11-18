from datetime import datetime

event_name = input("Enter Event Title: ")
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

event_name_upper = event_name.upper()
event_datetime = datetime(year, month, day)

print(f"\nEvent: {event_name_upper}")
print(f"Date: {event_datetime.strftime('%B %d, %Y')}")
print(f"Year: {year}")
print(f"Month: {event_datetime.strftime('%B')}")
print(f"Day: {day}")
print(f"Weekday: {event_datetime.strftime('%A')}")
