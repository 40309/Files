#Tony K.
#09/02/2015
#File - C.E starter


#Remake 1
def get_test_results():
    test_results = []
    with open("test_data.txt",mode="r",encoding = "utf-8") as my_file:
        for number in my_file:
           test_results.append(number)
    return test_results           

def average_test_result(results):
    total = 0
    for test in results:
        total = total + test
    average = total/len(results)
    return average

def display_average_result(average):
    print("your average test result is: {0}".format(average))


def main():
    test_results = get_test_results()
    average = average_test_result(test_results)
    display_average_result(average)

if __name__ == "__main__":
    main()

