#used for shapes and method for each shape with a final method printing every single shape

from math import pi

print("This program calculates the area of multiple shapes. Select a shape and follow instructions. The default unit is cm.")

shapes = {
    "shape1":"Square (1)",
    "shape2":"Rectangle (2)",
    "shape3":"Triangle (3)",
    "shape4":"Circle (4)",
    "shape5":"parallelogram (5)",
    "shape6":"Rhombus (6)",
    "shape7":"Trapezoid (7)"
}

print(f"These are all the shapes this calculator can work with: {shapes}")
while True:
  try:
    calculation = int(input("Please enter the number which corresponds to the shape you want to work with: "))
    if 1 <= calculation <= 7:
        break
    print("Please enter a numer between 1 and 7.")
  except ValueError:
    print("Please enter a number.")

    

def calculate_square():
  side = float(input("Please enter the length of the side in cm: "))
  return side * side
  
def calculate_rectangle():
  length = float(input("Please enter the length in cm: "))
  width = float(input("Please enter the width in cm:"))
  return length * width
  
def calculate_triangle():
  base = float(input("Please enter the base in cm: "))
  height = float(input("Please enter the height in cm: "))
  return (base * height)/2
 
def calculate_circle():
  radius = float(input("Please enter the radius in cm: "))
  return pi * radius**2
  
def calculate_parallelogram():
  parallelogram_base = float(input("Please enter the base in cm: "))
  height = float(input("Please enter the height in cm: "))
  return parallelogram_base * height
  
def calculate_rhombus():
  diagonal_1 = float(input("Please enter the length of the first diagonal in cm: "))
  diagonal_2 = float(input("Please enter the length of the second diagonal in cm: "))
  return (diagonal_1 * diagonal_2)/2
  

def calculate_trapezoid():
  parallel_side_1 = float(input("Please enter the length of the first parallel side in cm: "))
  parallel_side_2 = float(input("Please enter the length of the second parallel side in cm: "))
  height = float(input("Please enter the height in cm: "))
  return 0.5 * ((parallel_side_1 + parallel_side_2) * height)
  

def calculator(calculation):

  if calculation == 1:
    result = calculate_square()
    print(f"The area of the square is {result} cm^2.")

  elif calculation == 2:
    result = calculate_rectangle()
    print(f"The area of the rectangle is {result} cm^2.")

  elif calculation == 3:
    result = calculate_triangle()
    print(f"The area of the triangle is {result} cm^2.")

  elif calculation == 4:
    result = calculate_circle()
    print(f"The area of the circle is {result} cm^2.")

  elif calculation == 5:
    result = calculate_parallelogram()
    print(f"The area of the parallelogram is {result} cm^2.")

  elif calculation == 6:
    result = calculate_rhombus()
    print(f"The area of the rhombus is {result} cm^2.")

  else:
    result = calculate_trapezoid()
    print(f"The area of the trapezoid is {result} cm^2.")

calculator(calculation)
 
