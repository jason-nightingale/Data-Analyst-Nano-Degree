"""This script uses inputs from 1 and up on each input, splits the values
by the commas, runs a simulated if you hand in the missing homework
before the end of the year. Then prints out a supposed email for each
inputed name entered. We are also zipping the inputs together"""

names = input("Enter in a list of names: ")
assignments = input("Enter in the number of missing assignments for each name: ")
grades = input("What are their current grades for each name: ")

for name, assignment, grade in zip(names.title().split(","), assignments.split(","), grades.split(",")):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
    new_grade = int(float(grade)) + int(float(assignment)) * 2
    print(message.format(name, assignment, grade, new_grade))
