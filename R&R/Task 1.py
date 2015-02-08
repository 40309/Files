with open("students.txt", mode="r", encoding="utf-8") as students:
    count = 1
    for student in students:
        print("{0}. {1}".format(count,student))
        count = count + 1
