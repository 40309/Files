#Tony K.
#10/02/2015
#CE - Development Execercise Task 1
import pickle

with open ("task 1.bat" , mode = "wb") as my_file:
    user_name = input("Please enter our full name: ")
    user_dob = int(input("Please enter your date of birth (YYYY-MM-DD): "))
    pickle.dump(user_name, my_file)
    pickle.dump(user_dob, my_file)
