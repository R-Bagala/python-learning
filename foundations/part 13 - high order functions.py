#A closure is basically when a function is defined in another function
#The inner function references variables from the outer function
#the outer function returns the inner function 
#It needs to be stored somewhere(closure result) as it only returns the inner


#closure example
def circle_circumference():
    multiplier = 2
    def calculation(radius):
        return multiplier * pi * radius
    return calculation

closure_result = circle_circumference()
print(closure_result(8))

#decorators are simply functions that remember variables from an outer scope like decorators but the variable is another function 

#example decorator

from math import sqrt as sqrt

def sqrt_decorator(function): #parameter is whatever function I pass into it to add new features
    def wrapper():
        func = function() #func holds the result 6
        square_root = sqrt(func) #take the result 6 and squareroot it
        return square_root
    return wrapper

        


@sqrt_decorator #the same as calculation = sqrt_decorator(calculation)
def calculation(): #triggers wrapper
    return 6+10
print(calculation())

def add_10(function):
    def wrapper():
        func = function()
        added_10 = func + 10
        return added_10
    return wrapper

@add_10
def addition():
    return 50
print(addition())


#So basically, the function parameter next to the sqrt_decorator is the calculation method.
#takes the function(calculation) and adds new features to it under the wrapper

#map() function is a function that takes a function and iterable as parameters
numbers = [60, 50, 40, 30.2, 55, 88, 99]
square_root = map(lambda x: sqrt(x), numbers 2:.F)
print(list(square_root))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

excercise_4 = [country for country in countries]
excercise_5 = [name for name in names]
excercise_6 = [number for number in numbers]
#print(f"countries: {excercise_4}, names: {excercise_5} and numbers: {excercise_6}")

#excerciselevel 2: 1.

 
capitals = map(lambda x: x.upper(), countries)
print(list(capitals))

#2.

squared = map(lambda x: x**2, numbers)
print(list(squared))

#3.

capital_names = map(lambda name: name.upper(), names)
print(list(capital_names))

#4.

def countries_with_land(country):
    if country.endswith("land"):
        return False
    
    return True

countries_without_land = filter(countries_with_land, countries)
print(list(countries_without_land))

#5

def six_characters(country):
    if len(country) >=6:
        return False
    return True

countries_without_6 = filter(six_characters, countries)
print(list(countries_without_6))

#6

def countries_with_E(country):
    if country.startswith("E"):
        return False
    
    return True

countries_without_E = filter(countries_with_E, countries)
print(list(countries_without_E))

#8

#def get_string_list(list):
    #new_list = [i for i in list  type(i) == str]
    #return new_list

#print(get_string_list([12, 4, 5, 4, 6, 5, 99, "hello", "Hi"]))

#9

from functools import reduce

def add_numbers(x, y):
    return int(x) + int(y)

total = reduce(add_numbers, numbers)
print(total)

#10

def country_concatenate(x, y):
    return str(x) + ", " + str(y) 

new_countries = countries[:5]

concatenation = reduce(country_concatenate, new_countries)
print(f"{concatenation} and iceland are north european countries.")