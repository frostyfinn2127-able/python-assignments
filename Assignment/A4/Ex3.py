numbers = []
text = input("Enter a number (or press Enter to quit): ")
while text != "":
    numbers.append(int(text))
    text = input("Enter a number (or press Enter to quit): ")
if len(numbers) > 0:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
else:
    print("You didn't enter any numbers.")