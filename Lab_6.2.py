"""
Create a Python file named lab_6-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a variable my_row and set it equal to a list that contains the names of 2 people in your row.
Using slices, add your name to the end of the list.
Create another variable my_row2 and set it equal to my_row.
Add a statement that prints my_row2
Add a statement that removes the value at index 1 from my_row
Add a statement that prints my_row. What do you notice happens and why?

"""
#Alsir Elsheikh 11/7/2023
# These are the people in my row and using this code it deletes Jacobs name from the final printed statement
my_row = ["Rinvil", "Jacob"]
my_row = my_row + ["Alsir"]
my_row2 = my_row
print("my_row2:", my_row2)
del my_row[1]
print("my_row:", my_row)
#I noticed that the name Jacob is removed because the statement i made deletes his name from the final printed product which was at index 1.
