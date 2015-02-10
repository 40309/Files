#Tony K.
#10/02/2015
#CE - Development Execercise Task 1
import pickle

with open ("task 1.bat" , mode = "wb") as my_file:
    user = []
    user_name = input("Please enter our full name: ")
    user.append(user_name)
    user_dob = input("Please enter your date of birth (YYYY-MM-DD): ")
    user.append(user_dob)
    pickle.dump(user, my_file)
