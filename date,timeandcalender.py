from datetime import date , time , datetime

today=date.today()
now=datetime.now()
print("Today's date:", today)
print("\nCurrent date and time:", now)

print("data components:", today.day, today.month, today.year)