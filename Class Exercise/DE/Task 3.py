#Tony K.
#10/02/2015
#CE - Development Execercise Task 3

import pickle

with open ("task 1.bat" , mode = "wb") as my_file:
    user = []
    user_name = input("Please enter your full name: ")
    user_dob = input("Please enter your date of birth (YYYY-MM-DD): ")
    user.append(user_name)
    user.append(user_dob)
    pickle.dump(user, my_file)

print()

with open ("task 1.bat" , mode = "rb") as my_file:
    file_data = pickle.load(my_file)
    #print user_name
    print("Name: {0}".format(file_data[0]))
    #print dob
    print("Date Of Birth: {0}".format(file_data[1]))
