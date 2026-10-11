attempts = 0
logged_in = False
while attempts < 5 and not logged_in:
    username = input("Username: ")
    password = input("Password: ")
    if username == "finn" and password == "404":
        logged_in = True
    else:
        attempts += 1
        print("Wrong username or password")
if logged_in:
    print("Welcome")
else:
    print("Access denied")