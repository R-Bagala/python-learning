#adds 2 numbers
import math
def add_two_numbers(number_1, number_2):
  return number_1 + number_2

#circle area
def area_of_circle(radius):
  return pi * (radius ** 2)

#*members is a arbritrary parameter meaning no pre defined number of arguments
def print_name(group, *members):
  print(f"{group}'s members include: ")
  for i in members:
    print(i)

def add_all_nums(*nums):
  total = 0
  for i in nums:
    total += i
  return total

def convert_celcius_to_fahrenheit(Celcius):
  Fahrenheit = (Celcius * 9/5) + 32
  return Fahrenheit

def season(month):

  if month in ["January", "February", "March", "April"]:
    return "Spring"
  elif month in ["May", "June", "July"]:
    return "Summer"
  elif month in ["August", "September", "October"]:
    return "Fall"
  elif month in ["November", "December"]:
    return "Winter"
  else:
    return "Invalid Input"

def slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)


def quadratic_equation(a, b, c):
  x_1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2 * a)
  x_2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2 * a)

  return (f"The answer is either {x_1} or {x_2}.")


fruits = ["Orange", "Apple", "Banana", "Mango"]
numbers = [1, 4, 5, 7, 8, 9, 10]

def add_items(lst, item_to_add):
  lst.append(item_to_add)
def remove_items(lst, item_to_remove):
  lst.remove(item_to_remove)

add_items(fruits, "Pineapple")
remove_items(fruits, "Orange")
#print(fruits)


def sum_of_numbers(sum_number):
  sum = 0
  for i in range(sum_number + 1):
   sum += i
  return sum
#print(sum_of_numbers(5))
#print(sum_of_numbers(30))

def sum_of_odds(number_for_adding):
  sum = 0
  for i in range (number_for_adding + 1):
    if i % 2 != 0:
      sum += i
  return sum
#print(sum_of_odds(11))

def sum_of_evens(number):
  sum = 0
  for i in range(number + 1):
    if i % 2 == 0:
      sum += i
  return sum
#print(sum_of_evens(90))

def evens_and_odds(number):
  evens = 0
  odds = 0
  for i in range(number + 1):
    if i % 2 == 0:
      evens += 1
    elif i % 2 != 0:
      odds += 1
  return (f"The number of evens across all numbers up to {number} is {evens} and the number of odds is {odds}.")
#print(evens_and_odds(10))
