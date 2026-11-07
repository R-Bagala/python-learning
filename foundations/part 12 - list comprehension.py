language = "Python"
lst = [i for i in language]
print(lst)

password = "hello there"
password_list = [i for i in password]
print(password_list[0:5])

odd_numbers = [i for i in range(100) if  i % 2 != 0]
print(odd_numbers)

power = lambda a: a**2
print(power(2))

full_name = lambda a,b: a+b
print(full_name("Rob", "Tom"))

#excercises for day 13

from tkinter import N


numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
findings = [i for i in numbers if i <= 0 ]
#print(findings)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

old_list = [5, 6,7, 8, 11, 22, 44, 56, 77, 89]
new_list = [i for i in old_list]
print(new_list)

question_3 = [(i, 1, i, i*i, i*(i*i), i*(i*i*i), i*(i*i*i*i)) for i in range(11)]
print(question_3)

#question_4

countries = [[("Italy", "Rome")], [("Sweden", "Stockholm")], [("France", "Paris")]]


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
#print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#question_5

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Olso")]]
flattened_countries = [country for row in countries for country in row]
new_countries = [(set(i)) for i in flattened_countries]
#print(new_countries)

#question_6

names = [[("Thomas", "S")], [("Wade", "S")], [("Aiden", "B")]]
flattened_names = [name for person in names for name in person]
new_names = [i for i in names]
#print(new_names) to be continued

#question_7

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
#print(slope(5550, 6000, 7000, 9000))

