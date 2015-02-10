#Tony K.
#10/02/2015
#CE - Development Execercise Task 2
import pickle

class student:
    def __int__(self):
        self.name = None
        self.dob = None

student_list = []
sudents = student()
for each in range(2):
    student.name = input("Please enter your full name: ")
    student.dob = input("Please enter your date of birth (YYYY-MM-DD): ")
    student_list.append(student())


with open ("task 2.bat" , mode = "wb") as my_file:
    pickle.dump(student_list, my_file)
