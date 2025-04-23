userscore = input("Enter your score: ")
userscore = int(userscore)
if userscore >= 90:
    print("You got an A")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
elif age < 18:
    print("teenager")
price = 12 if age >= 18 else 8
print(price)