class food:
    pass

sausage = food()
#print(sausage)

class car:
    def __init__(this, brand, model, year, top_speed):
        this.brand = brand
        this.model = model
        this.year = year
        this.top_speed = top_speed

    def car_info(this):
        return f"The brand is {this.brand}, {this.model} is the model, its year is {this.year} and its top speed is {this.top_speed}."

car1 = car("Ferrari", "LaFerrari", 2014, 217 )
#print(car1.car_info()) 

#class with pre_defined values

class Person:
    def __init__(this, firstname = "Thomas", lastname = "Tomato", age = 52, city = "Rome", country = "Italy"):
        this.firstname = firstname
        this.lastname = lastname
        this.age = age
        this.city = city
        this.country = country

    def person_info(this):
        return f"{this.firstname} is their firstname, {this.lastname} is their lastname, they are {this.age} years old and live in {this.city}, {this.country}."


person1 = Person()
#print(person1.person_info())
person2 = Person("Boris", "Banana", 36, "Paris", "France")
#print(person2.person_info())

import statistics

class stats_calc:
    def __init__(this, lst = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]):
        this.lst = lst

    def count(this):
        return len(this.lst)

    def sum(this):
        return sum(this.lst)

    def min(this):
        return min(this.lst)

    def max(this):
        return max(this.lst)

    def range(this):
        return max(this.lst) - min(this.lst)

    def mean(this):
        return statistics.mean(this.lst)

    def median(this):
        return statistics.median(this.lst)

    def mode(this):
        return statistics.mode(this.lst) 

    def stan_dev(this):
        return statistics.stdev(this.lst)   

data = stats_calc()
print(data.count())
print(data.sum())
print(data.min())
print(data.max())
print(data.range())
print(data.mean())
print(data.median())
print(data.mode())
print(data.stan_dev())


data2 = stats_calc([4, 5, 6, 7, 8, 9, 10])
#print(data2.count())
