with open("new_animals.txt", mode="w",encoding="utf-8") as my_file:
        my_file.write("John"+"\n")
        my_file.write("Tony"+"\n")

with open("new_animals.txt", mode="r", encoding="utf-8") as students:
    count = 1
    for student in students:
        print("{0}. {1}".format(count,student))
        count = count + 1
