numbers = []

text = input("Enter a number (or press Enter to quit): ")
while text != "":
    numbers.append(int(text))
    text = input("Enter a number (or press Enter to quit): ")
numbers.sort(reverse=True)
print(numbers[:5])