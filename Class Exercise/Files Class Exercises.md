#Class Exercises - Files
These tasks are designed to help you practice the knowledge and skills you have developed. There are exercises to help you revise and develop your understanding and also to challenge you further.

##Saving Time
Often you will need to test your program. Until now you have to type in the test data every time you rerun the program.

This is obviously inefficient. Using a text file to store your test data would make more sense...

###Task 1
Open the python file called `test_data_exercise.py` and the text file `test_data.txt`.

![](https://www.dropbox.com/s/s180w5eubo8v11h/test_scores.jpg?dl=1)

Improve the code so that it uses the values stored in the text file to test the program rather than relying on user input.

##Syntax

```python
with open("myfile.txt",mode="r",encoding="utf-8") as my_file:
#opens text file for reading

with open("myfile.txt",mode="w",encoding="utf-8") as my_file:
#opens text file for writing

with open("myfile.txt",mode="a",encoding="utf-8") as my_file:
#opens text file for appending to the end of file

my_file.write("hello world")
#writes the text "hello world" to the file

my_file.write("hello world" + "\n")
#writes the text "hello world" as a line of text (next write will start on a new line

with open("myfile.txt",mode="rb") as my_file:
#opens binary file for reading

with open("myfile.txt",mode="wb") as my_file:
#opens binary file for writing

file_data = pickle.load(my_file)
#reads contents of binary file into a list

pickle.dump(file_data,my_file)
#writes contents of a list to a binary file
```

##Vocabulary

- **text file** - A file containing characters that can be edited in any text editor.
- **binary file** - A file containing data that can only be interpreted by your Python programs.
- **pickle** - The module required to deal with binary files.
- **exception** - This is what occurs when a program crashes with a traceback message
- **csv** - common separated values - a text file that has well understood formatting.

##Class Exercises
In this section you may choose the exercises you attempt. There are three types of exercises to consider:

1. **Revision Exercises** - choose these exercises if you are not confident in your understanding of selection statements
2. **Development Exercises** - choose these exercises if you are confident in your understanding but want some more practice
3. **Stretch and Challenge Exercises** - choose these exercises if you feel you have mastered selection and want to tackle some tougher problems

Once you feel more confident attempt some of the more difficult exercises. The more practice you get now the more comfortable you will be using selection in more complex programs later in the course.

Remember, practice makes perfect!

###Attempting These Exercises
You should do the following for each exercise you attempt:

1. Create **flowcharts** first - plan your solution on paper before attempting it
2. Create a set of **test data** - select values you will enter to test the program and know beforehand what you expect the answers to be
3. Write the **program** - write the program in Python using the pseudocode to assist you and the test data to ensure the program functions correctly

###Revision Exercises
Attempt these tasks if you need to build your confidence and understanding of file handling.

1. Write a program that reads in 5 lines of text the user types in at the keyboard. As each line is typed in, the program should write the line to a text file.**Done**
2. Write a program that reads lines of text from a text file and displays them to the user. You can create a text file in any text editor. Save it in the same folder as the code for the program. Remember to check for the end of the file.**Done**

###Development Exercises
Attempt these tasks if you are confident in your understanding but feel you need more practice

1. Write a program that reads a name and date of birth typed in at the keyboard and saves it as a list to a binary file.**Done**
2. Extend your program from the exercise above to read in several names and dates of birth. Allow the user to terminate the input by pressing the Enter key without typing in a name.**Done**
3. Write a program that reads the file created in exercise 3 and displays the name and date of birth.**Done**
4. Write a program that reads the file created in exercise 4 and displays the names and dates of birth as a table.

###Stretch and Challenge Exercises
Stretch and challenge exercises
Attempt these tasks if you feel you have mastered selection and want to tackle tougher problems.

1. Write a program that reads the file created in exercise 4 until it finds a specified name.

    The program should then display the name and corresponding date of birth. The program should display a suitable message if the name cannot be found in the file.

2. Write a program that will delete a specified entry from the file created in exercise 4.

    **Note**: You cannot just delete an entry from a binary file. You will need to copy all the entries to a list and perform the deletion there.

3. Create a binary file with records in alphabetical order of name. Now write a program that will add a record in the correct position in the file.

    **Note**: You cannot insert a record in a binary file. You will need to copy all the entries to a list and perform the insertion there.

4. Write a program that reads the file created in exercise 9 and searches for a specified name. If the name does not exist in the file, the program should abort the search at the earliest possible time and display a suitable message.

5. Write a program that will display a set of options to the user to add, delete or search for an entry in a given file. Use the programs developed above to produce a fully working system.

    **Note**: This exercise is a good opportunity to practice making functions and to make use of the linear search algorithm.