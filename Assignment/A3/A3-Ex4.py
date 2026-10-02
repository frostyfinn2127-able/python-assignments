year = int(input("Enter the year: "))
if year % 4 == 0 or year % 400 == 0:
    print("This is the leap year.")
else:
    print("This is not the leap year.")