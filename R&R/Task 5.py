checker = False

while checker == False:
    try:
        user_input = int(input("Please enter a number between 1-100: "))
    except ValueError:
        print("The value entered was not a number")
    if user_input < 1:
        print("The number you entered is too low, Try again")
    elif user_input > 100:
        print("The number you entered is too high, Try again")
    else:
        print()
        print("The Number you entered is good")
        print(user_input)
        checker = True

print()
print()
print("End of Program")
