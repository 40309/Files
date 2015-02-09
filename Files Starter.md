#Starter - Files
These tasks are designed to refresh the reading and research you have undertaken at home prior to this lesson. If you have not completed the R&R assignment then please speak to your teacher before attempting these exercises.

##Modes and encoding
You have been introduced the the various file opening modes that are used in Python. Refresh your knowledge of these concepts by attempting the below tasks.

###Task 1

|Mode|Explanation|
|----|-----------|
|`a`|*Append data to what already exists*|
|`w`|*Writes on the File (deletes previous data in the file) or create a new file*|
|`r`|*Read the data from the file*|

###Task 2
You must set the encoding parameter when opening a file. Identify the encoding method you should use and in the space provided explain why:

|Encoding|Explanation|
|--------|-----------|
|utf-8|*The file encoding language is platform dependent.*|

##Reading from a file
The screenshot below shows the result of reading in the names of students from a file and then printing them to the screen.

![](https://www.dropbox.com/s/ds7b5mddim5z4fh/students.jpg?dl=1)

The code for printing the students to the screen is shown below:

```python
for index student in enumerate(student_file):
    print("{0:>2}. {1}".format(index+1, student))
```

###Task 3
For the above code, explain what each of the following sections of code do:

|Section|Explanation|
|-------|-----------|
|`index`|*A numbered list*|
|`{0:>2}`|*align he characters with a column of numbers *|

###Task 4
In the above screenshot there are gaps between each student in the list. It should look like the screenshot below.

![](https://www.dropbox.com/s/ozsch3ylpr4prrh/students2.jpg?dl=1)

**Attempt** to explain why there are gaps between each student and then suggest how the above code could be improved to remove them.

**Space for your answer:**

*Because  he print statement also prints a blank line*

```python
for index student in enumerate(student_file):
    print("{0:>2}. {1}".format(index+1, student),end="")
```

##Exception Handling
Exception Handling is used to deal with **known errors** in a more elegant manor than crashing the program. Take a look at the following code:

```python
try:
    score = int(input(“Please enter your score: “)
except:
    print(“Please enter an integer value only”)
print(Your score was {0}”.format(score))
```

###Task 5
**Identify** and **explain** (without running the code) all of the errors in this code

|Error|Explanation|
|-----|-----------|
|*No **Value Error** Error*|*No Error was specified*|
| | |
| | |
| | |
| | |





> Written with [StackEdit](https://stackedit.io/).