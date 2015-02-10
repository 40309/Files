#Tony K.
#10/02/2015
#CE - Revision Task 1


with open ("task 1.txt" , mode = "w" , encoding = "utf-8") as my_file:
    for count in range(5):
        my_file.write(input("Please enter your message: ")+ "\n")

