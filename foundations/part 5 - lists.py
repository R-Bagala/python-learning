#lists

#we are able to use a *rest function to print "the rest" of a list. We can call the rest variable anything
fruits = ["apple", "orange", "banana", "lemon", "tomato", "mango"]
fruit1, fruit2, *rest_of_fruits, last_fruit = fruits
print(fruit1)
print(fruit2)
#print(rest_of_fruits)
#print(last_fruit)

breakfast = ["eggs", "bacon", "sausages", "hashbrowns", "beans", "toast"]
first, second, *double, third, fourth = breakfast
first = "black pudding (ew!)"
print(first)
print(second)
#print(double)
#print(third)
#print(fourth)

bands = ["Queen", "Led Zeppelin", "Black Sabbath", "Pink Floyd"]
bands[1] = "The Beatles"
#print(bands)
does_exist = "Queen" in bands #for checking if a value exists
print(does_exist)

#for adding items to an already existing list without removing any
#print(bands)

#for inserting into a certain position
bands.insert(3, "Soundgarden")
#print(bands)

#for removing through name and index (using pop)
bands.remove("Queen")
bands.pop(1)
#print(bands)

#when we want to clear a list completely
#bands.clear()
#print(bands)

#copying list using .copy function and joining lists together
new_bands = bands.copy()
bands.extend(new_bands)
print(bands)
bands.count("The Beatles") #counts how many ttimes an item appears on a list
print(bands.index("Soundgarden"))
print(bands.count("The Beatles"))
bands.sort() #sorts strings in alphabetical order and numbers in numerical order
print(bands)

numbers = [4, 1, 7, 5, 6, 7, 9, 1, 10, 200, 500, 71, 1000, 567, 67]
numbers.sort()
print(numbers.count(1))
print(numbers)