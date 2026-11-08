#"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
#"a" - Append - Opens a file for appending(adds at the end), creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)





#use forward slash not backslash
f = open("C: 3 excercises.txt")
text = f.read()#.splitlines() #reads the document itself. Splitlines does the same as readlines().
first_line = f.readline() #reads the first line
long_line = f.readlines()
print(text)
print(first_line)
print(long_line) #prints every line but puts all the lines in long lines instead of printing it by the lines in the actual doc.

#adding new stuff to files
with open("C:/day 3 excercises.txt", "a") as f:
    f.write("This will appear at the end")#will write and you don't have to write print statements after

import os

os.path.exists("print (3 != 2).txt")

import json

#change a json to dictionary (a JSON is a string form of a dictionary)
json_variable = '''{
    "Name_1": "John", 
    "Name_2": "Doe"
}'''

print(type(json))
dictionary = json.loads(json_variable) #change json to dictionary. To change a dictionary to json we use json.dumps()
print(type(dictionary))

import csv
with open("well.csv.xlsx") as f:
    csv_reader = csv.reader(f, delimiter =",")
    

